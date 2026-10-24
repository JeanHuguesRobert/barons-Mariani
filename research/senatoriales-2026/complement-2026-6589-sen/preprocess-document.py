#!/usr/bin/env python3
"""Deterministic Markdown projection; preview keeps PILOTAGE, institutional output strips it."""
import argparse
import json
import re
from pathlib import Path

DIRECTIVE = re.compile(r"<!--\s*#pragma\s+(TODO|META|INCLUDE|FORMAT|PILOTAGE)\b([\s\S]*?)-->", re.I)
ANY_PRAGMA = re.compile(r"<!--\s*#pragma\b", re.I)
UNSAFE = re.compile(r"<!--\s*(?:INTERNAL-TODO|INTERNAL-META)\b[\s\S]*?-->", re.I)
BLOCK = re.compile(r"<!--\s*(?:INTERNAL-TODO|INTERNAL-META)\b", re.I)
FORMAT_DIRECTIVE = re.compile(r"<!--\s*#pragma\s+FORMAT\b([\s\S]*?)-->", re.I)


class PreprocessError(ValueError):
    pass


def parse_format_spec(payload):
    try:
        spec = json.loads(payload.strip())
    except json.JSONDecodeError as exc:
        raise PreprocessError("FORMAT requires a valid JSON object") from exc
    if not isinstance(spec, dict) or set(spec) != {"profile", "plain_text", "pdf"}:
        raise PreprocessError("FORMAT requires profile, plain_text, and pdf settings")
    if spec["profile"] != "rfc7994":
        raise PreprocessError("unsupported plain-text profile")
    plain = spec["plain_text"]
    pdf = spec["pdf"]
    if not isinstance(plain, dict) or set(plain) != {
        "columns", "page_lines", "toc_depth", "bom", "form_feed"
    }:
        raise PreprocessError("FORMAT plain_text settings do not match the supported schema")
    if plain["columns"] != 72 or plain["page_lines"] != 58:
        raise PreprocessError("RFC 7994 layout requires 72 columns and 58 lines per page")
    if plain["bom"] is not True or plain["form_feed"] is not True:
        raise PreprocessError("RFC 7994 text output requires a UTF-8 BOM and form-feed pagination")
    if not isinstance(pdf, dict) or set(pdf) != {"toc_depth"}:
        raise PreprocessError("FORMAT pdf settings do not match the supported schema")
    for value in (plain["toc_depth"], pdf["toc_depth"]):
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 6:
            raise PreprocessError("FORMAT toc_depth must be an integer from 1 through 6")
    return spec


def read_format_spec(path):
    source = Path(path).read_text(encoding="utf-8")
    matches = list(FORMAT_DIRECTIVE.finditer(source))
    if len(matches) != 1:
        raise PreprocessError(f"expected one FORMAT directive, found {len(matches)}")
    return parse_format_spec(matches[0].group(1))


def transform(path, target="institutional", stack=()):
    path = Path(path).resolve()
    if target not in ("institutional", "preview", "work"):
        raise PreprocessError("unknown target")
    if path in stack:
        raise PreprocessError("cyclic INCLUDE: " + str(path))
    source = path.read_text(encoding="utf-8")
    if target == "work":
        return source
    if BLOCK.search(source) and not UNSAFE.search(source):
        raise PreprocessError("unclosed INTERNAL annotation")

    # Legacy INTERNAL-TODO/INTERNAL-META comments are supported.
    source = UNSAFE.sub("", source)
    def substitute(match):
        kind, value = match.group(1).upper(), match.group(2).strip()
        if kind in ("TODO", "META"):
            return ""
        if kind == "PILOTAGE":
            return value if target == "preview" else ""
        if kind == "FORMAT":
            parse_format_spec(value)
            return ""
        if not value or not value.startswith("path:"):
            raise PreprocessError("INCLUDE requires 'path: relative/file.md'")
        relative = value.removeprefix("path:").strip()
        child = (path.parent / relative).resolve()
        if child.suffix.lower() != ".md" or not child.is_relative_to(path.parent):
            raise PreprocessError("INCLUDE must be a Markdown file under source directory")
        return transform(child, target, (*stack, path))
    output = DIRECTIVE.sub(substitute, source)
    if ANY_PRAGMA.search(output) or BLOCK.search(output) or "-->" in output and "<!-- #pragma" in output:
        raise PreprocessError("unknown or malformed internal directive")
    return output


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--target", choices=["institutional", "preview", "work"], required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    generated = transform(args.source, args.target)
    output = args.output.resolve()
    if output == args.source.resolve():
        raise SystemExit("refusing to overwrite source")
    if output.exists():
        raise SystemExit("refusing to overwrite existing output")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generated, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Minimal deterministic Markdown source processor. No transmission or PDF generation."""
import argparse
import re
from pathlib import Path

DIRECTIVE = re.compile(r"<!--\s*#pragma\s+(TODO|META|INCLUDE)\b([\s\S]*?)-->", re.I)
ANY_PRAGMA = re.compile(r"<!--\s*#pragma\b", re.I)
UNSAFE = re.compile(r"<!--\s*(?:INTERNAL-TODO|INTERNAL-META)\b[\s\S]*?-->", re.I)
BLOCK = re.compile(r"<!--\s*(?:INTERNAL-TODO|INTERNAL-META)\b", re.I)


class PreprocessError(ValueError):
    pass


def transform(path, target="institutional", stack=()):
    path = Path(path).resolve()
    if target not in ("institutional", "work"):
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
    ap.add_argument("--target", choices=["institutional", "work"], required=True)
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

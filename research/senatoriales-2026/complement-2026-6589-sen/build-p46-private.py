#!/usr/bin/env python3
"""Build a PRIVATE P-46 textual collection from 46 exported .eml files.

Never publish the output or the input files to a public repository.
No network or automatic mail transmission is performed.
"""
from __future__ import annotations
import argparse
from email import policy
from email.parser import BytesParser
from pathlib import Path
import re

PRIVATE_TAGS = ("[ADRESSE PRIVÉE OCCULTÉE]", "[SECRET OCCULTÉ]")
def redact(text: str, additional: list[str]) -> str:
    # Generic redaction is a *first pass* only; require manual validation.
    for value in additional:
        if value:
            text = text.replace(value, PRIVATE_TAGS[0])
    # Conservatively redact bearer-style links and obvious token arguments.
    text = re.sub(r"(?i)([?&](?:token|access_token|signature|key|password|code)=)[^\s&#]+",
                  r"\1" + PRIVATE_TAGS[1], text)
    return text

def first_plain(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and part.get_content_disposition() != "attachment":
                return part.get_content()
        raise ValueError("No text/plain body: requires controlled HTML conversion")
    if msg.get_content_type() != "text/plain":
        raise ValueError("No text/plain body")
    return msg.get_content()

def build(directory: Path, destinations: Path, substitutions: list[str]) -> None:
    destinations.parent.mkdir(parents=True, exist_ok=True)
    items = []
    for n in range(1, 47):
        path = directory / f"P-46.{n:02}.eml"
        if not path.is_file():
            raise FileNotFoundError(f"Missing required source {path}")
        msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        text = first_plain(msg)
        attachments = [(p.get_filename() or "[sans nom]") for p in msg.walk()
                       if p.get_content_disposition() == "attachment"]
        item = (f"P-46.{n:02}\n"
                f"Date: {msg.get('Date', '')}\n"
                f"From: {msg.get('From', '')}\n"
                f"To: {msg.get('To', '')}\n"
                f"Cc: {msg.get('Cc', '')}\n"
                f"Subject: {msg.get('Subject', '')}\n"
                f"Attachments ({len(attachments)}): {', '.join(attachments) or 'none'}\n"
                "\n" + text + "\n")
        items.append(redact(item, substitutions))
    joined = "\n" + ("=" * 68) + "\n"
    # Refuse public-output defaults; caller must choose PRIVATE output path.
    destinations.write_text(
        "RECUEIL PRIVÉ EN COURS DE RELECTURE — NE PAS TRANSMETTRE NI PUBLIER\n"
        "Occultation automatique provisoire ; contrôle humain nécessaire.\n\n"
        + joined.join(items), encoding="utf-8")
    print("46/46 EML parsed; private draft produced; NOT validated for disclosure")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eml-dir", type=Path, required=True)
    ap.add_argument("--private-output", type=Path, required=True)
    ap.add_argument("--redact-literal", action="append", default=[],
                    help="Literal private identifier to redact, no value stored in source")
    args = ap.parse_args()
    if any(part in {"repos", "github", ".git"} for part in args.private_output.parts):
        raise SystemExit("Refusing destination inside a repository-oriented path")
    build(args.eml_dir, args.private_output, args.redact_literal)

if __name__ == "__main__":
    main()

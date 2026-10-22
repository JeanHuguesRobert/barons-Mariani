#!/usr/bin/env python3
"""Build a PRIVATE P-46 textual collection from 46 exported .eml files.

Never publish the output or the input files to a public repository.
No network or automatic mail transmission is performed.
"""
from __future__ import annotations
import argparse
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
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

class PlainTextFromHtml(HTMLParser):
    """Convert HTML-only email bodies to inert text without fetching resources."""
    BLOCKS = {"address", "article", "blockquote", "br", "dd", "div", "dl", "dt",
              "h1", "h2", "h3", "h4", "h5", "h6", "hr", "li", "ol", "p",
              "pre", "section", "table", "td", "th", "tr", "ul"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.suppressed = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "head"}:
            self.suppressed += 1
        elif not self.suppressed and tag in self.BLOCKS:
            self.parts.append("\n")
            if tag == "li":
                self.parts.append("• ")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "head"} and self.suppressed:
            self.suppressed -= 1
        elif not self.suppressed and tag in self.BLOCKS:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.suppressed:
            self.parts.append(data)


def html_to_text(source: str) -> str:
    parser = PlainTextFromHtml()
    parser.feed(source)
    parser.close()
    text = "".join(parser.parts)
    text = re.sub(r"[ \t\v\f]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not text:
        raise ValueError("HTML body converted to empty text")
    return text


def first_plain(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and part.get_content_disposition() != "attachment":
                return part.get_content()
        for part in msg.walk():
            if part.get_content_type() == "text/html" and part.get_content_disposition() != "attachment":
                return html_to_text(part.get_content())
        raise ValueError("No readable text/plain or text/html body")
    if msg.get_content_type() != "text/plain":
        if msg.get_content_type() == "text/html":
            return html_to_text(msg.get_content())
        raise ValueError("No readable text/plain or text/html body")
    return msg.get_content()

def build(directory: Path, destinations: Path, substitutions: list[str]) -> None:
    validate_private_output(destinations)
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
    # Do not create output directories until every required source has parsed.
    destinations.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents an accidental overwrite of an earlier bundle.
    with destinations.open("x", encoding="utf-8", newline="\n") as output:
        output.write(
            "RECUEIL PRIVÉ EN COURS DE RELECTURE — NE PAS TRANSMETTRE NI PUBLIER\n"
            "Occultation automatique provisoire ; contrôle humain nécessaire.\n\n"
            + joined.join(items))
    print("46/46 EML parsed; private draft produced; NOT validated for disclosure")

def validate_private_output(destination: Path) -> None:
    """Reject output paths inside this repository, including resolved symlinks."""
    repo_root = Path(__file__).resolve().parents[3]
    target = destination.resolve()
    if target == repo_root or repo_root in target.parents:
        raise SystemExit("Refusing output inside the public source repository")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eml-dir", type=Path, required=True)
    ap.add_argument("--private-output", type=Path, required=True)
    ap.add_argument("--redact-literal", action="append", default=[],
                    help="Literal private identifier to redact, no value stored in source")
    args = ap.parse_args()
    build(args.eml_dir, args.private_output, args.redact_literal)

if __name__ == "__main__":
    main()

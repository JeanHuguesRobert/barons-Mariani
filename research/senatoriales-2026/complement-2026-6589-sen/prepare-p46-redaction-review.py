#!/usr/bin/env python3
"""Create a private, preliminary minimization copy of the P-46 text bundle.

This is a review aid, not a disclosure approval. The source bundle is preserved.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

EMAIL = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
PHONE = re.compile(r"(?<!\w)(?:\+33|0033|0)[ .-]?(?:[1-9](?:[ .-]?\d{2}){4})(?!\w)")
STREET = re.compile(
    r"(?i)\b\d{1,4}\s+(?:rue|avenue|av\.|boulevard|bd\.|chemin|route|place|"
    r"impasse|lieu-dit|cours)\s+[^\n,;]{1,70}"
)
ATTACHMENTS = re.compile(r"(?m)^(Attachments \(\d+\): ).*$")


def prepare(source: str) -> tuple[str, dict[str, int]]:
    text = source
    counts = {
        "email_address": len(EMAIL.findall(text)),
        "phone_candidate": len(PHONE.findall(text)),
        "street_address_candidate": len(STREET.findall(text)),
        "attachment_filename_list": len(ATTACHMENTS.findall(text)),
    }
    text = EMAIL.sub("[COURRIEL OCCULTÉ]", text)
    text = PHONE.sub("[TÉLÉPHONE OCCULTÉ]", text)
    text = STREET.sub("[ADRESSE OCCULTÉE]", text)
    text = ATTACHMENTS.sub(r"\1[noms de pièces jointes occultés pour revue]", text)
    notice = (
        "PROPOSITION DE MINIMISATION AUTOMATIQUE — NON VALIDÉE POUR COMMUNICATION\n"
        "Les noms de personnes, identifiants de documents et autres données sensibles "
        "ne sont pas tous détectables automatiquement.\n"
        "Les originaux RFC822 restent les seules sources ; contrôle humain requis avant "
        "intégration ou transmission.\n\n"
    )
    return notice + text, counts


def ensure_outside_repo(destination: Path, repo_root: Path) -> None:
    target = destination.resolve()
    root = repo_root.resolve()
    if target == root or root in target.parents:
        raise ValueError("Refusing to write private P-46 data inside the repository")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True,
                    help="Private compiled P-46 text bundle")
    ap.add_argument("--output", type=Path, required=True,
                    help="Private destination for the review copy")
    args = ap.parse_args()
    ensure_outside_repo(args.output, repo_root)
    journal = args.output.with_name(args.output.stem + "-redaction-journal.json")
    if args.output.exists() or journal.exists():
        raise FileExistsError("Review copy or journal already exists; refusing overwrite")
    candidate, counts = prepare(args.source.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(candidate)
    with journal.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump({"source": args.source.name, "candidate": args.output.name,
                   "status": "unreviewed", "redactions": counts},
                  stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(f"Private preliminary copy created: {args.output}")
    print(f"Redaction counts (values omitted): {json.dumps(counts, ensure_ascii=False)}")
    print("Names, identity data and context require human review; NOT cleared for disclosure.")


if __name__ == "__main__":
    main()

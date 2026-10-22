#!/usr/bin/env python3
"""Create a P-46 copy masking only explicitly configured private email addresses."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

EMAIL = re.compile(r"(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}")


def prepare(source: str, private_addresses: list[str]) -> tuple[str, dict[str, int]]:
    if not private_addresses:
        raise ValueError("Configure Laurence and Maguy's private addresses outside the repository")
    text = source
    counts = {"private_email_address": 0}
    for address in dict.fromkeys(item.strip() for item in private_addresses):
        if not EMAIL.fullmatch(address):
            raise ValueError("Invalid configured private email address")
        text, count = re.subn(re.escape(address), "[ADRESSE PRIVÉE OCCULTÉE]", text,
                              flags=re.IGNORECASE)
        counts["private_email_address"] += count
    notice = (
        "COPIE P-46 — adresses privées de Laurence et Maguy occultées selon la règle "
        "de communication fixée par le requérant.\n"
        "Tout le reste du texte, y compris les autres adresses courriel, numéros, adresses "
        "postales et noms de pièces jointes, est conservé sans transformation.\n"
        "Cette copie textuelle ne remplace pas les EML RFC822 natifs.\n\n"
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
    ap.add_argument("--private-addresses", type=Path, required=True,
                    help="Private UTF-8 file with Laurence and Maguy email addresses, one per line")
    ap.add_argument("--output", type=Path, required=True,
                    help="Private destination for the review copy")
    args = ap.parse_args()
    ensure_outside_repo(args.output, repo_root)
    ensure_outside_repo(args.private_addresses, repo_root)
    if not args.private_addresses.is_file():
        raise FileNotFoundError("Private address configuration file not found")
    journal = args.output.with_name(args.output.stem + "-redaction-journal.json")
    if args.output.exists() or journal.exists():
        raise FileExistsError("Review copy or journal already exists; refusing overwrite")
    private_addresses = [
        line.strip() for line in args.private_addresses.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    candidate, counts = prepare(args.source.read_text(encoding="utf-8"), private_addresses)
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
    print("Only configured private addresses were masked; all other source text was retained.")


if __name__ == "__main__":
    main()

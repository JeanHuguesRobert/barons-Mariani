#!/usr/bin/env python3
"""Build traceable, non-frozen editorial bundles from a checked-out Corpus snapshot.

A source change triggers the preview workflow; this script does not publish releases.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "living-books-news"
SOURCE = "research/autonomia/observatoire_processus_autonomie_corse.md"
BOOKS = {
    "capable": "projects/capable/editions/2026-10-09-en-preparation.md",
    "suicide-corse": "projects/suicide-corse/editions/2026-10-09-n4-en-preparation.md",
    "1755": "projects/1755/editions/2026-10-09-rc1-en-preparation.md",
}
def digest(b):
    return hashlib.sha256(b).hexdigest()

def main():
    source = ROOT / SOURCE
    if not source.is_file():
        raise SystemExit("missing source: " + SOURCE)
    source_bytes = source.read_bytes()
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema": "living-books.news-preview/v1",
        "status": "working-unfrozen-not-published",
        "source": SOURCE,
        "source_sha256": digest(source_bytes),
        "git_sha": os.environ.get("GITHUB_SHA", "local"),
        "built_at_utc": datetime.now(timezone.utc).isoformat(),
        "books": [],
    }
    for book, src in BOOKS.items():
        p = ROOT / src
        if not p.is_file():
            raise SystemExit("missing edition plan: " + src)
        data = p.read_bytes()
        rel = book + "-en-preparation.md"
        header = ("# Aperçu documentaire — " + book + "\n\n"
                  "> **EN PRÉPARATION — non gelé, non publié comme édition.** "
                  "Ce paquet est une synthèse de provenance, non un livre rendu.\n\n"
                  "Source : " + SOURCE + " (SHA-256: " + digest(source_bytes) + ")\n\n"
                  "État éditorial : " + src + " (SHA-256: " + digest(data) + ")\n\n"
                  "Le contenu vérifié, les inconnues et les corrections appartiennent "
                  "à l'Observatoire et ne doivent pas être inventés ici.\n\n---\n\n")
        (OUT / rel).write_text(header + data.decode("utf-8"), encoding="utf-8")
        manifest["books"].append({"id": book, "input": src, "sha256": digest(data), "preview": rel})
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Built", len(BOOKS), "unfrozen editorial previews:", OUT)

if __name__ == "__main__":
    main()

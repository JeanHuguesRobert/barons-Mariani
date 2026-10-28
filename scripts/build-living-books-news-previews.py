#!/usr/bin/env python3
"""Public, unfrozen and traceable living-book working editions.

Generated pages are public projections. Never edit frozen editions.
"""
from pathlib import Path
from html import escape
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "previews" / "en-preparation"
BOOKS = {
    "capable": {
        "edition": "projects/capable/editions/2026-10-28-projection-candidate-n1.md",
        "chapters": [
            "projects/capable/manuscript/00-ouverture.md",
            "projects/capable/manuscript/01-capable-est-un-adjectif.md",
            "projects/capable/manuscript/02-subsidiarite-rendue-effective.md",
            "projects/capable/manuscript/03-effectivite.md",
            "projects/capable/manuscript/04-liberte-egalite-fraternite-effectives.md",
            "projects/capable/manuscript/05-machines-et-correction.md",
            "projects/capable/manuscript/06-fractalite-et-echelles.md",
            "projects/capable/manuscript/07-campagnes-comme-reality-tests.md",
            "projects/capable/manuscript/08-presidentielle-2027.md",
            "projects/capable/manuscript/09-communs-et-moyens.md",
            "projects/capable/manuscript/10-capable-test.md",
        ],
        "magazine": [
            "projects/capable/magazine/2026-10-28-autonomie-corse.md",
            "projects/capable/magazine/2026-10-28-campagne-du-reel-et-presentations.md",
            "projects/capable/magazine/2026-10-28-energie-et-capacites-territoriales.md",
            "projects/capable/magazine/2026-10-28-genese-capable.md",
            "projects/capable/magazine/2026-10-28-procedures-et-effectivite.md",
            "projects/capable/magazine/2026-10-28-retrospective-notes-de-campagne.md",
        ],
        "annexes": [
            "projects/capable/annexes/2026-10-28-dossiers-a1-a4.md",
            "projects/capable/annexes/2026-10-28-dossiers-a5-a8.md",
        ],
    },
    "suicide-corse": {
        "edition": "projects/suicide-corse/editions/2026-10-09-n4-en-preparation.md",
        "chapters": [],
    },
    "1755": {
        "edition": "projects/1755/editions/2026-10-09-rc1-en-preparation.md",
        "chapters": ["projects/1755/manuscript/n1/05-epilogue-lheritage-et-les-possibles-contemporains.md"],
    },
    "rise-and-fall": {
        "edition": "projects/rise-and-fall/issues/2026-10-26-revolutions-lumineuses/README.md",
        "chapters": [
            "projects/rise-and-fall/issues/2026-10-26-revolutions-lumineuses/livre.md",
            "projects/rise-and-fall/issues/2026-10-26-revolutions-lumineuses/magazine.md",
            "projects/rise-and-fall/issues/2026-10-26-revolutions-lumineuses/annexes.md",
            "projects/rise-and-fall/issues/2026-10-26-revolutions-lumineuses/passerelles.md",
        ],
    },
}
COMMON = ["research/autonomia/observatoire_processus_autonomie_corse.md",
          "research/autonomia.md",
          "research/methode_terrains_feconds.md",
          "research/noyau_doctrinal_rendre_capable.md"]

def md_body(raw):
    if raw.startswith("---\n"):
        _, sep, tail = raw.partition("\n---\n")
        if sep:
            return tail.lstrip()
    return raw

def to_html(md):
    # Faithful, readable source display; no untrusted Markdown HTML execution.
    lines = []
    for line in md_body(md).splitlines():
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            n = len(m.group(1))
            lines.append(f"<h{n}>{escape(m.group(2))}</h{n}>")
        elif not line.strip():
            lines.append("<div class='space'></div>")
        else:
            lines.append("<p>{}</p>".format(escape(line)))
    return "\n".join(lines)

def digest(b):
    return hashlib.sha256(b).hexdigest()

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"schema": "living-books.public-working/v1",
                "status": "public-en-preparation-non-gele",
                "books": []}
    index = ["<h1>Livres Vivants — versions publiques en préparation</h1>",
             "<p>Versions évolutives, non gelées. Les éditions gelées restent distinctes.</p>"]
    for name, cfg in BOOKS.items():
        paths = [cfg["edition"]] + cfg["chapters"] + cfg.get("magazine", []) + cfg.get("annexes", [])
        sections, inputs = [], []
        for path in paths:
            data = (ROOT / path).read_bytes()
            inputs.append({"path": path, "sha256": digest(data)})
            title = ("Sommaire candidat" if path == cfg["edition"] else
                     "Livre — " + Path(path).stem if path in cfg["chapters"] else
                     "Magazine — " + Path(path).stem if path in cfg.get("magazine", []) else
                     "Annexes — " + Path(path).stem if path in cfg.get("annexes", []) else Path(path).stem)
            sections.append(f"<section><h2>{escape(title)}</h2>"
                f"<small><a href='https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/{escape(path)}'>Source versionnée</a></small>"
                + to_html(data.decode("utf-8")) + "</section>")
        css = "<style>body{font:17px/1.65 Georgia,serif;max-width:820px;margin:35px auto;padding:0 20px;color:#202733}h1,h2,h3{font-family:system-ui}h2{margin-top:2em}section{border-top:1px solid #ddd}small,.meta{color:#555}.space{height:.4em}p{overflow-wrap:anywhere}</style>"
        book_digest = digest(json.dumps(inputs, sort_keys=True).encode("utf-8"))
        body = f"<h1>{escape(name)} — en préparation</h1><p class='meta'>PUBLIC · NON GELÉ · empreinte des sources {book_digest}</p>"
        body += "<p>Cette page rend le travail éditorial consultable. Elle ne constitue pas une édition définitive. Les sources liées font foi ; les inconnues demeurent ouvertes.</p>"
        body += "\n".join(sections)
        out = "<!doctype html><html lang='fr'><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>"+escape(name)+" — en préparation</title>"+css+"<body>"+body+"</body></html>"
        (OUT / (name + ".html")).write_text(out, encoding="utf-8")
        manifest["books"].append({"id": name, "page": name + ".html", "source_sha256": book_digest, "inputs": inputs})
        index.append(f"<p><a href='{escape(name)}.html'>{escape(name)} — en préparation</a></p>")
    manifest["related_sources"] = [{"path": p, "sha256": digest((ROOT / p).read_bytes())} for p in COMMON]
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "index.html").write_text("<!doctype html><html lang='fr'><meta charset='utf-8'><title>Livres Vivants en préparation</title><body>"+"\n".join(index)+"</body></html>", encoding="utf-8")
    print("Built", len(BOOKS), "public working edition pages in", OUT)

if __name__ == "__main__":
    main()

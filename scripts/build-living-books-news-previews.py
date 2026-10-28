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

def to_html(md, source_path="", included=()):
    """Safe minimal Markdown renderer: headings, links, emphasis and lists."""
    import posixpath
    def inline(value):
        parts = re.split(r'(\[[^\]\n]+\]\([^)]+\)|\*\*[^*\n]+\*\*)', value)
        rendered = []
        for part in parts:
            m = re.fullmatch(r'\[([^\]\n]+)\]\(([^)]+)\)', part)
            if m:
                label, url = m.groups()
                if not url.startswith(("https://", "http://", "#")):
                    target = posixpath.normpath(posixpath.join(posixpath.dirname(source_path), url))
                    url = ("#" + source_anchor(target) if target in included else
                           "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/" + target)
                rendered.append('<a href="' + escape(url, quote=True) + '">' + escape(label) + '</a>')
            elif part.startswith("**") and part.endswith("**"):
                rendered.append("<strong>" + escape(part[2:-2]) + "</strong>")
            else:
                rendered.append(escape(part))
        return "".join(rendered)
    lines, items, kind = [], [], None
    def flush():
        nonlocal kind
        if items:
            lines.append("<" + kind + ">" + "".join(items) + "</" + kind + ">")
            items.clear()
            kind = None
    code_lines = []
    table_rows = []
    in_code = False
    def flush_table():
        if not table_rows:
            return
        rows = [r.strip().strip("|").split("|") for r in table_rows]
        if len(rows) > 1 and all(re.fullmatch(r"[-: ]+", c.strip()) for c in rows[1]):
            rows.pop(1)
        html_rows = []
        for n, cells in enumerate(rows):
            tag = "th" if n == 0 else "td"
            html_rows.append("<tr>" + "".join("<" + tag + ">" + inline(c.strip()) + "</" + tag + ">" for c in cells) + "</tr>")
        lines.append("<div class='table-scroll'><table>" + "".join(html_rows) + "</table></div>")
        table_rows.clear()
    for line in md_body(md).splitlines():
        if line.lstrip().startswith("```"):
            flush()
            flush_table()
            if in_code:
                lines.append("<pre><code>" + escape("\n".join(code_lines)) + "</code></pre>")
                code_lines.clear()
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(line)
            continue
        if line.strip().startswith("|") and line.strip().endswith("|"):
            flush()
            table_rows.append(line)
            continue
        flush_table()
        if line.startswith("> "):
            flush()
            lines.append("<blockquote>" + inline(line[2:]) + "</blockquote>")
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        numbered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if heading:
            flush()
            n = len(heading.group(1))
            lines.append(f"<h{n}>" + inline(heading.group(2)) + f"</h{n}>")
        elif bullet or numbered:
            next_kind = "ul" if bullet else "ol"
            if kind != next_kind:
                flush()
                kind = next_kind
            items.append("<li>" + inline((bullet or numbered).group(1)) + "</li>")
        elif not line.strip():
            flush()
        else:
            flush()
            lines.append("<p>" + inline(line) + "</p>")
    flush()
    flush_table()
    if in_code:
        lines.append("<pre><code>" + escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(lines)

def source_anchor(path):
    return "source-" + hashlib.sha256(path.encode("utf-8")).hexdigest()[:12]

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
        included = set(paths)
        for path in paths:
            data = (ROOT / path).read_bytes()
            inputs.append({"path": path, "sha256": digest(data)})
            title = ("Sommaire candidat" if path == cfg["edition"] else
                     "Livre — " + Path(path).stem if path in cfg["chapters"] else
                     "Magazine — " + Path(path).stem if path in cfg.get("magazine", []) else
                     "Annexes — " + Path(path).stem if path in cfg.get("annexes", []) else Path(path).stem)
            sections.append(f"<section id='{source_anchor(path)}'><h2>{escape(title)}</h2>"
                f"<small><a href='https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/{escape(path)}'>Source versionnée</a></small>"
                + to_html(data.decode("utf-8"), path, included) + "</section>")
        css = "<style>body{font:17px/1.65 Georgia,serif;max-width:820px;margin:35px auto;padding:0 20px;color:#202733}*{box-sizing:border-box}nav{display:flex;gap:.8rem;flex-wrap:wrap;padding:.75rem 0}a{overflow-wrap:anywhere}section{scroll-margin-top:1rem}@media(max-width:600px){body{font-size:16px;margin:14px auto;padding:0 14px}h1{font-size:1.65em}h2{font-size:1.28em}pre{font-size:.85em}}h1,h2,h3{font-family:system-ui}h2{margin-top:2em}section{border-top:1px solid #ddd}blockquote{border-left:3px solid #888;padding-left:1em;color:#454545}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f4f4;padding:1em}.table-scroll{overflow-x:auto}table{border-collapse:collapse;width:100%}td,th{padding:.4em;border:1px solid #ccc;text-align:left}small,.meta{color:#555}.space{height:.4em}p{overflow-wrap:anywhere}</style>"
        book_digest = digest(json.dumps(inputs, sort_keys=True).encode("utf-8"))
        body = f"<h1>{escape(name)} — en préparation</h1><p class='meta'>PUBLIC · NON GELÉ · empreinte des sources {book_digest}</p>"
        body += "<p>Cette page rend le travail éditorial consultable. Elle ne constitue pas une édition définitive. Les sources liées font foi ; les inconnues demeurent ouvertes.</p>"
        body += "<nav aria-label='Parties'><a href='#" + source_anchor(cfg["chapters"][0]) + "'>Livre</a> · <a href='#" + source_anchor(cfg.get("magazine", cfg["chapters"])[0]) + "'>Magazine</a> · <a href='#" + source_anchor(cfg.get("annexes", cfg["chapters"])[0]) + "'>Annexes</a></nav>" if name == "capable" else ""
        body += "\n".join(sections)
        out = "<!doctype html><html lang='fr'><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>"+escape(name)+" — en préparation</title>"+css+"<body>"+body+"</body></html>"
        # Fail the build if a generated local anchor is absent or duplicated.
        ids = re.findall(r"""\bid=['"]([^'"]+)['"]""", out)
        anchors = re.findall(r"""href=['"]#([^'"]+)['"]""", out)
        if len(ids) != len(set(ids)):
            raise ValueError(f"{name}: duplicate section IDs")
        missing = sorted(set(anchors) - set(ids))
        if missing:
            raise ValueError(f"{name}: unresolved local anchors: {missing}")
        (OUT / (name + ".html")).write_text(out, encoding="utf-8")
        manifest["books"].append({"id": name, "page": name + ".html", "source_sha256": book_digest, "inputs": inputs})
        index.append(f"<p><a href='{escape(name)}.html'>{escape(name)} — en préparation</a></p>")
    manifest["related_sources"] = [{"path": p, "sha256": digest((ROOT / p).read_bytes())} for p in COMMON]
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "index.html").write_text("<!doctype html><html lang='fr'><meta charset='utf-8'><title>Livres Vivants en préparation</title><body>"+"\n".join(index)+"</body></html>", encoding="utf-8")
    print("Built", len(BOOKS), "public working edition pages in", OUT)

if __name__ == "__main__":
    main()

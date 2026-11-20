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
            "projects/capable/magazine/2026-11-13-qui-choisit-agenda-politique.md",
            "projects/capable/magazine/2026-11-13-ia-contradiction-et-autonomie.md",
            "projects/capable/magazine/2026-11-13-bleu-de-chine-appartenances.md",
            "projects/capable/magazine/2026-11-20-pacte-republicain-effectivite.md",
            "projects/capable/magazine/2026-10-05-epreuve-de-l-effectivite.md",
            "projects/capable/magazine/historique/2026-10-02-n1-lancement-campagne-presidentielle.md",
            "projects/capable/magazine/historique/2026-10-05-jalon-p1-p18-matrice-eim.md",
            "projects/capable/magazine/historique/2026-10-05-lancement-du-mouvement-capable.md",
        ],
        "cases": [
            "projects/capable/cases/README.md",
            "projects/capable/cases/case-01-kouchner-acces-dossier-medical.md",
            "projects/capable/cases/case-02-parrainages-presidentiels-verrou-rural.md",
            "projects/capable/cases/case-03-dalo-droit-au-logement-sans-toit.md",
            "projects/capable/cases/case-04-consignation-radars-automatiques.md",
            "projects/capable/cases/case-05-dematerialisation-service-public-rural.md",
        ],
        "annexes": [
            "projects/capable/annexes/2026-10-28-dossiers-a1-a4.md",
            "projects/capable/annexes/2026-10-28-dossiers-a5-a8.md",
            # Public, unfreezed normative/doctrinal sources of the November candidate.
            "projects/capable/doctrine/revision_constitutionnelle_article_72.md",
            "projects/capable/doctrine/pacte-republicain-effectivite.md",
            "research/devise_republicaine/etat_chantier_2026-11-20.md",
            "projects/capable/campaign/marche-du-soleil.md",
            "projects/capable/campaign/observatoire-presentations-2027.md",
            "projects/capable/doctrine/metaprogramme-politique-generatif.md",
            "research/autonomia/grammaire_autonomie_de_capacite.md",
            "projects/capable/annexes/2026-11-13-recherches-decisions-et-objections.md",
        ],
    },
    "suicide-corse": {
        "edition": "projects/suicide-corse/editions/2026-10-09-n4-en-preparation.md",
        "chapters": [],
    },
    "1755": {
        "edition": "projects/1755/editions/2026-10-09-rc1-en-preparation.md",
        "chapters": ["projects/1755/manuscript/n1/05-epilogue-lheritage-et-les-possibles-contemporains.md"],
        "cases": [
            "projects/1755/cases/case-01-dieta-generale-1755.md",
            "projects/1755/cases/case-02-reception-transnationale-boswell.md",
        ],
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

def to_html(md, source_path="", included=(), *, reader_chapter=False):
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
    skipped_first_heading = False
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
            if reader_chapter and n == 1 and not skipped_first_heading:
                skipped_first_heading = True
                continue
            level = min(6, n + 2) if reader_chapter else n
            lines.append(f"<h{level}>" + inline(heading.group(2)) + f"</h{level}>")
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

def chapter_title(source):
    """Use the author's visible title, not a file stem or a technical label."""
    text = md_body(source)
    match = re.search(r"^# ([^\n]+)", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "Document de travail"


def render_capable(paths, cfg):
    """Accessible reading path; archives and editing notes remain available."""
    chapter_set = set(cfg["chapters"])
    magazine_set = set(cfg["magazine"])
    case_set = set(cfg["cases"])
    annexes_set = set(cfg["annexes"])
    included = set(paths)
    inputs = []
    content = {}
    for path in paths:
        data = (ROOT / path).read_bytes()
        inputs.append({"path": path, "sha256": digest(data)})
        content[path] = data.decode("utf-8")
    book_digest = digest(json.dumps(inputs, sort_keys=True).encode("utf-8"))

    def source_link(path):
        return ("https://github.com/JeanHuguesRobert/barons-Mariani/"
                "blob/main/" + path)

    def section(path):
        source = content[path]
        title = chapter_title(source)
        link = escape(source_link(path), quote=True)
        flag = ("<p class='source-status'>Archive d'octobre 2026 : texte de travail, "
                "pas un numéro publié.</p>" if "/magazine/historique/" in path else
                "<p class='source-status'>Dossier de travail : faits et qualifications "
                "encore à vérifier.</p>" if path in case_set else "")
        # Source identification also lets the installed canonical deployer
        # verify ordering without displaying a filename to the visitor.
        source_label = "Livre — 00-ouverture" if path == chapters[0] else ""
        source_attribute = (f" data-source='{escape(source_label, quote=True)}'"
                            if source_label else "")
        return (f"<section id='{source_anchor(path)}' class='chapter'{source_attribute}>"
                f"<h3>{escape(title)}</h3>{flag}"
                f"<p class='source-link'><a href='{link}'>Consulter le texte et ses sources sur GitHub</a></p>"
                + to_html(source, path, included, reader_chapter=True)
                + "</section>")

    def toc(paths):
        return "<ol class='toc'>" + "".join(
            f"<li><a href='#{source_anchor(path)}'>{escape(chapter_title(content[path]))}</a></li>"
            for path in paths
        ) + "</ol>"

    archive_magazine = [p for p in cfg["magazine"] if "/magazine/historique/" in p]
    current_magazine = [p for p in cfg["magazine"] if p not in archive_magazine]
    chapters = cfg["chapters"]
    part_nav = (
        "<nav aria-label='Parties du Livre Vivant'>"
        "<a href='#part-livre'>Le Livre</a>"
        "<a href='#part-magazine'>Le Magazine</a>"
        "<a href='#part-cases'>Cas du Réel</a>"
        "<a href='#part-annexes'>Annexes</a>"
        "<a href='#part-edition'>Notes éditoriales</a>"
        "</nav>"
    )
    parts = [
        "<header><h1>Capable — Le Livre Vivant</h1>"
        "<p class='lead'>Liberté, Égalité, Fraternité. Pour de vrai.</p>"
        "<p>Comment rendre les droits et les libertés réellement accessibles ? "
        "Ce Livre examine ce que les personnes et les territoires peuvent faire, "
        "ce qui les en empêche et comment vérifier les effets des décisions.</p>"
        "<p class='meta'>Version publique en préparation, révisable. "
        "<strong>Aucun numéro Capable n'a encore été définitivement arrêté.</strong></p>"
        "</header>",
        "<div class='reading-guide'><p><strong>Comment lire ?</strong> "
        "Le <em>Livre</em> explique les idées qui doivent durer ; le <em>Magazine</em> "
        "raconte et analyse des événements datés ; les <em>Cas du Réel</em> "
        "examinent des situations concrètes ; les <em>Annexes</em> permettent "
        "de consulter les propositions, les sources et les éléments à vérifier. "
        "Vous pouvez commencer par le Livre sans connaître le projet.</p></div>",
        part_nav,
        "<div class='part-intro' id='part-livre'><h2>Le Livre — comprendre Capable</h2>"
        "<p>Onze chapitres pour découvrir les idées, leurs usages et leurs limites.</p>"
        + toc(chapters) + "</div>",
        "".join(section(path) for path in chapters),
        "<div class='part-intro' id='part-magazine'><h2>Le Magazine — faits et débats datés</h2>"
        "<p>Des chroniques sur la Corse, la démocratie, les outils numériques, "
        "les territoires et les engagements du mouvement. "
        "Les faits vérifiés y sont distingués des opinions et des projets.</p>"
        + toc(current_magazine) + "</div>",
        "".join(section(path) for path in current_magazine),
        "<details class='archive'><summary>Archives de lancement d'octobre 2026 "
        "(trois textes de travail, aucun numéro publié)</summary>"
        "<p>Ces documents conservent les formulations de départ, même quand elles "
        "ne correspondent plus exactement au projet actuel.</p>"
        + "".join(section(path) for path in archive_magazine) + "</details>",
        "<div class='part-intro' id='part-cases'><h2>Cas du Réel — cinq dossiers concrets</h2>"
        "<p>Ces recherches portent notamment sur l'accès aux documents médicaux, "
        "le logement, les démarches administratives et les présentations "
        "des candidats à la présidentielle. Elles restent ouvertes à la vérification.</p></div>",
        "".join(section(path) for path in cfg["cases"]),
        "<div class='part-intro' id='part-annexes'><h2>Annexes — textes et preuves</h2>"
        "<p>Pour aller plus loin : dossiers de recherche, projet de révision "
        "constitutionnelle, méthode et état de l'étude historique de la devise.</p>"
        + toc(cfg["annexes"]) + "</div>",
        "".join(section(path) for path in cfg["annexes"]),
        "<details id='part-edition' class='editorial'>"
        "<summary>Note de composition du numéro — notes de fabrication et historique de cette version</summary>"
        + section(cfg["edition"]) + "</details>",
        "<footer class='edition-footer'><p>Édition de travail composée à partir de "
        + str(len(paths)) + " sources versionnées. "
        "Leur liste, leurs dates et leurs empreintes figurent dans "
        "<a href='https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/"
        "previews/en-preparation/manifest.json'>le manifeste public</a>. "
        "Empreinte de cet assemblage : <code>" + book_digest +
        "</code>.</p><p><a href='#part-livre'>Revenir au début du Livre</a></p></footer>"
    ]
    css = """<style>
*{box-sizing:border-box}body{font:17px/1.7 Georgia,serif;max-width:880px;margin:2rem auto;padding:0 1.5rem;color:#26313c;background:#fff}
h1,h2,h3,h4,h5,h6,nav,summary,.meta,.source-link,.source-status{font-family:system-ui,sans-serif}
h1{font-size:2.1rem;line-height:1.2}h2{font-size:1.65rem}h3{font-size:1.35rem}h4{font-size:1.12rem}
p,li{overflow-wrap:anywhere}a{color:#185b8c;text-underline-offset:.12em}
nav{display:flex;flex-wrap:wrap;gap:.8rem;padding:1rem 0;border-block:1px solid #ccd1d5}
nav a{white-space:nowrap}.lead{font-size:1.25rem;font-weight:bold}.meta,.source-link,.source-status{font-size:.85rem;color:#48515b}
.part-intro{border-top:3px solid #303d4c;margin-top:3rem;padding-top:.7rem;scroll-margin-top:1rem}
.chapter{border-top:1px solid #d8dee3;margin-top:2rem;padding-top:.7rem;scroll-margin-top:1rem}
.chapter h3{margin-bottom:.25rem}.source-link{margin-top:0}
.reading-guide{border-left:3px solid #556b7d;padding:.2rem 1.1rem;margin:2rem 0;background:#f7f9fa}
.toc{columns:2;column-gap:2rem;padding-left:1.3rem;font-family:system-ui,sans-serif;font-size:.95rem}
.toc li{break-inside:avoid;margin:.35rem 0}
details{margin:2rem 0;padding:1rem 1.15rem;border:1px solid #c9d0d6;border-radius:.4rem}
summary{cursor:pointer;font-weight:600}
.archive,.editorial{background:#fafbfc}
blockquote{border-left:3px solid #89939d;margin:1rem 0;padding:.2rem 1rem;background:#fafafa}
pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f2f4f5;padding:1rem}
.table-scroll{overflow-x:auto}table{border-collapse:collapse;width:100%}td,th{padding:.45rem;border:1px solid #c5ccd3;text-align:left}
.edition-footer{margin:3rem 0;border-top:1px solid #cdd4da;padding-top:1rem;font-size:.85rem;color:#4c5560}
code{overflow-wrap:anywhere}@media(max-width:600px){body{font-size:16px;margin:0 auto;padding:0 1rem}.toc{columns:1}h1{font-size:1.7rem}h2{font-size:1.4rem}}
</style>"""
    result = ("<!doctype html><html lang='fr'><meta charset='utf-8'>"
              "<meta name='viewport' content='width=device-width'>"
              "<title>Capable — Le Livre Vivant en préparation</title>"
              + css + "<body>" + "\n".join(parts) + "</body></html>")
    return result, inputs, book_digest


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"schema": "living-books.public-working/v1",
                "status": "public-en-preparation-non-gele",
                "books": []}
    index = ["<h1>Livres Vivants — versions publiques en préparation</h1>",
             "<p>Versions évolutives de travail. Aucun gel éditorial n’est déduit de la mise en ligne.</p>"]
    for name, cfg in BOOKS.items():
        if name == "capable":
            paths = (cfg["chapters"] + cfg.get("magazine", []) +
                     cfg.get("cases", []) + cfg.get("annexes", []) + [cfg["edition"]])
            out, inputs, book_digest = render_capable(paths, cfg)
        else:
            paths = ([cfg["edition"]] + cfg["chapters"] + cfg.get("magazine", []) +
                     cfg.get("cases", []) + cfg.get("annexes", []))
            sections, inputs = [], []
            included = set(paths)
            for path in paths:
                data = (ROOT / path).read_bytes()
                inputs.append({"path": path, "sha256": digest(data)})
                title = ("Note de composition du numéro" if path == cfg["edition"] else
                         "Livre — " + Path(path).stem if path in cfg["chapters"] else
                         "Magazine — " + Path(path).stem if path in cfg.get("magazine", []) else
                         "Cas du Réel — " + Path(path).stem if path in cfg.get("cases", []) else
                         "Annexes — " + Path(path).stem if path in cfg.get("annexes", []) else Path(path).stem)
                sections.append(f"<section id='{source_anchor(path)}'><h2>{escape(title)}</h2>"
                    f"<small><a href='https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/{escape(path)}'>Source versionnée</a></small>"
                    + to_html(data.decode("utf-8"), path, included) + "</section>")
            css = "<style>body{font:17px/1.65 Georgia,serif;max-width:820px;margin:35px auto;padding:0 20px;color:#202733}*{box-sizing:border-box}nav{display:flex;gap:.8rem;flex-wrap:wrap;padding:.75rem 0}a{overflow-wrap:anywhere}section{scroll-margin-top:1rem}@media(max-width:600px){body{font-size:16px;margin:14px auto;padding:0 14px}h1{font-size:1.65em}h2{font-size:1.28em}pre{font-size:.85em}}h1,h2,h3{font-family:system-ui}h2{margin-top:2em}section{border-top:1px solid #ddd}blockquote{border-left:3px solid #888;padding-left:1em;color:#454545}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f4f4;padding:1em}.table-scroll{overflow-x:auto}table{border-collapse:collapse;width:100%}td,th{padding:.4em;border:1px solid #ccc;text-align:left}small,.meta{color:#555}.space{height:.4em}p{overflow-wrap:anywhere}</style>"
            book_digest = digest(json.dumps(inputs, sort_keys=True).encode("utf-8"))
            body = f"<h1>{escape(name)} — en préparation</h1><p class='meta'>PUBLIC · NON GELÉ · empreinte des sources {book_digest}</p>"
            body += "<p>Cette page rend le travail éditorial consultable. Elle ne constitue pas une édition définitive. Les sources liées font foi ; les inconnues demeurent ouvertes.</p>"
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

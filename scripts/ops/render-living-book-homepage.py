#!/usr/bin/env python3
"""Render an optional Living Book homepage and portable-AI orientation from JSON.

Source: projects/<book>/site/homepage.json (living-book-homepage/v1).
Output: static site/index.html, assistants.html, marche/index.html and homepage.css.
No networking, runtime account, third-party SDK or platform-specific prompt delivery.
"""
import argparse
from html import escape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
CSS = ROOT / "scripts/lib/living-book-homepage.css"


def e(value):
    return escape(str(value), quote=True)


def href(value):
    value = str(value)
    if not (value.startswith(("https://", "#")) or re.fullmatch(r"[A-Za-z0-9_./#-]+", value)):
        raise ValueError("Unsupported link target: " + value)
    if ".." in value.split("/"):
        raise ValueError("Unsafe path traversal: " + value)
    return e(value)


def anchor(item, css_class=""):
    css = f' class="{e(css_class)}"' if css_class else ""
    ext = ' target="_blank" rel="noopener noreferrer"' if str(item["href"]).startswith("https://") else ""
    return f'<a{css} href="{href(item["href"])}"{ext}>{e(item["label"])}<span aria-hidden="true"> ↗</span></a>'


def layout(title, description, canonical, content, nav, prefix=""):
    links = "".join(f'<a href="{prefix}{href(path)}">{e(label)}</a>' for label, path in nav)
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{href(canonical)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{href(canonical)}">
<link rel="stylesheet" href="{prefix}styles.css">
<link rel="stylesheet" href="{prefix}homepage.css">
</head>
<body class="capable-landing">
<a class="skip" href="#contenu">Aller au contenu principal</a>
<header class="site landing-nav">
 <p class="mark"><a href="{prefix}index.html">Capable</a></p>
 <nav aria-label="Navigation principale">{links}</nav>
</header>
<main id="contenu" class="landing-main">{content}</main>
<footer class="landing-footer">
 <p><strong>Capable</strong> · Le citoyen reste souverain. Les idées restent discutables.</p>
 <p><a href="{prefix}book.html">Le Livre</a> · <a href="{prefix}n1.html">Numéro 1</a> · <a href="{prefix}en-preparation.html">En préparation</a> · <a href="{prefix}sources.html">Sources</a> · <a href="{prefix}contribuer.html">Contribuer</a> · <a href="{prefix}mentions.html">Mentions</a></p>
</footer>
</body>
</html>
'''


def home(cfg):
    paths = "".join(
        f'''<article class="journey-card"><span class="journey-index">{e(p["number"])}</span>
<h3>{e(p["title"])}</h3><p>{e(p["description"])}</p>
{anchor({"label": p["label"], "href": p["href"]}, "card-action")}</article>'''
        for p in cfg["paths"]
    )
    principles = "".join(
        f'<article><h3>{e(p["title"])}</h3><p>{e(p["text"])}</p></article>'
        for p in cfg["principles"]
    )
    focus = cfg["focus"]
    body = f'''
<section class="hero-panel" aria-labelledby="headline">
 <p class="eyebrow">{e(cfg["kicker"])}</p>
 <h1 id="headline">{e(cfg["headline"])}</h1>
 <p class="hero-lead">{e(cfg["lead"])}</p>
 <p class="hero-description">{e(cfg["introduction"])}</p>
 <div class="action-row">{anchor(cfg["primary_action"], "action-primary")}{anchor(cfg["secondary_action"], "action-secondary")}</div>
</section>
<section class="focus-panel" id="marche" aria-labelledby="marche-title">
 <div><p class="eyebrow">{e(focus["eyebrow"])}</p><h2 id="marche-title">{e(focus["title"])}</h2>
 <p>{e(focus["text"])}</p></div>
 <div class="focus-actions">{anchor(focus["action"], "action-primary")}
 <a class="subtle-link" href="{href(focus["source_url"])}">Lire le document source</a></div>
</section>
<section id="explorer" aria-labelledby="explorer-title">
 <p class="eyebrow">VOUS CHOISISSEZ VOTRE PARCOURS</p>
 <h2 id="explorer-title">Trois façons d'explorer Capable</h2>
 <p>Aucun assistant imposé. Vous pouvez changer de chemin à tout moment.</p>
 <div class="journey-grid">{paths}</div>
</section>
<section id="comprendre" aria-labelledby="comprendre-title">
 <p class="eyebrow">DÉMOCRATIE ASSISTÉE PAR ORDINATEUR</p>
 <h2 id="comprendre-title">Accroître la capacité, jamais confisquer la décision</h2>
 <div class="principle-grid">{principles}</div>
 <p class="reading-link">Pour approfondir : <a href="book.html">le Livre Vivant</a> · <a href="guide.html">son Guide</a> · <a href="https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/capable/doctrine.md">la doctrine et ses sources</a></p>
</section>
'''
    nav = [("Accueil", "index.html"), ("La Marche", "marche/"), ("Avec mon IA", "assistants.html"),
           ("Guide", "guide.html"), ("Le Livre", "book.html"), ("Sources", "sources.html")]
    return layout(cfg["name"] + " — " + cfg["headline"], cfg["lead"], cfg["canonical_base"] + "/", body, nav)


def assistants(cfg):
    a = cfg["assistant"]
    providers = "".join(anchor(p, "provider-link") for p in a["providers"])
    prompt = e(a["prompt"])
    body = f'''
<section class="inner-page">
 <p class="eyebrow">DÉMOCRATIE ASSISTÉE PAR ORDINATEUR</p>
 <h1>{e(a["headline"])}</h1><p class="hero-lead">{e(a["lead"])}</p>
 <ol class="steps"><li>Choisissez l'assistant que vous utilisez habituellement.</li>
 <li>Copiez ce contexte dans votre conversation.</li>
 <li>Choisissez votre question, demandez des sources et faites-vous votre propre opinion.</li></ol>
 <div class="provider-list">{providers}<a class="provider-link" href="#contexte">Autre assistant</a></div>
 <div id="contexte" class="prompt-panel">
 <label for="prompt">Contexte à transmettre à votre assistant</label>
 <textarea id="prompt" rows="17" readonly>{prompt}</textarea>
 <button type="button" class="action-primary copy-button" id="copy-prompt">Copier le contexte</button>
 <span id="copy-status" role="status" aria-live="polite"></span>
 <p class="prompt-help">Le texte peut aussi être sélectionné et copié manuellement. Aucun dialogue n'est transmis par ce site.</p>
 </div>
 <p class="reading-link">Vous préférez un dialogue sur place ? <a href="guide.html">Ouvrir le Guide Capable</a>. Ou <a href="index.html">retourner à l'accueil</a>.</p>
</section>
<script>
(() => {{
  const button = document.getElementById('copy-prompt');
  const box = document.getElementById('prompt');
  const status = document.getElementById('copy-status');
  button.addEventListener('click', async () => {{
    try {{
      await navigator.clipboard.writeText(box.value);
      status.textContent = 'Contexte copié. Vous pouvez le coller dans votre assistant.';
    }} catch (_) {{
      box.focus(); box.select();
      status.textContent = 'Texte sélectionné : copiez-le avec Ctrl+C (ou le menu du navigateur).';
    }}
  }});
}})();
</script>
'''
    nav = [("Accueil", "index.html"), ("La Marche", "marche/"), ("Guide", "guide.html"), ("Le Livre", "book.html")]
    return layout("Avec mon IA — " + cfg["name"], a["lead"], cfg["canonical_base"] + "/assistants.html", body, nav)


def marche(cfg):
    focus = cfg["focus"]
    body = f'''
<section class="inner-page">
 <p class="eyebrow">MOUVEMENT CAPABLE · PRÉSIDENTIELLE 2027</p>
 <h1>{e(focus["title"])}</h1>
 <p class="hero-lead">{e(focus["text"])}</p>
 <h2>Deux objectifs distincts, une démarche ouverte</h2>
 <div class="principle-grid">
  <article><h3>Explorer les capacités</h3><p>Aller à la rencontre des habitants, écouter les obstacles et les solutions, documenter et confronter les observations.</p></article>
  <article><h3>Solliciter les élus</h3><p>Rencontrer des élus habilités à présenter un candidat, dans la perspective des 500 présentations requises pour l'élection présidentielle.</p></article>
  <article><h3>Rendre des comptes</h3><p>Distinguer contact, intérêt, promesse et présentation officiellement établie. Une intention n'est pas un résultat.</p></article>
 </div>
 <div class="focus-panel"><div><p class="eyebrow">PAGE DE TRANSITION</p><h2>Le parcours participatif est en construction</h2>
 <p>Cette page constitue le premier point d'entrée stable. Les outils interactifs de la Marche du Soleil seront raccordés ici lorsqu'ils seront prêts.</p></div>
 <div class="focus-actions"><a class="action-primary" href="{href(focus["source_url"])}">Lire la Marche du Soleil ↗</a>
 <a class="subtle-link" href="../assistants.html">L'explorer avec mon IA</a></div></div>
 <p class="reading-link"><a href="../index.html">Retour au Mouvement Capable</a> · <a href="../book.html">Découvrir le Livre Vivant</a></p>
</section>
'''
    nav = [("Accueil", "index.html"), ("Avec mon IA", "assistants.html"), ("Guide", "guide.html"), ("Le Livre", "book.html")]
    return layout("La Marche du Soleil — " + cfg["name"], focus["text"], cfg["canonical_base"] + "/marche/", body, nav, prefix="../")


def render(config_path):
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    if cfg.get("schema") != "living-book-homepage/v1":
        raise ValueError("Unsupported homepage schema")
    if not cfg.get("canonical_base", "").startswith("https://"):
        raise ValueError("canonical_base must be HTTPS")
    site = config_path.parent
    return {
        site / "index.html": home(cfg),
        site / "assistants.html": assistants(cfg),
        site / "marche" / "index.html": marche(cfg),
        site / "homepage.css": CSS.read_text(encoding="utf-8"),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path, help="Path to homepage.json")
    parser.add_argument("--check", action="store_true", help="Verify committed outputs match their sources")
    args = parser.parse_args()
    outputs = render(args.config.resolve())
    mismatches = []
    for path, content in outputs.items():
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                mismatches.append(str(path))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print("RENDER", path)
    if mismatches:
        print("OUT_OF_DATE", *mismatches, sep="\n", file=sys.stderr)
        return 1
    print("HOMEPAGE_CHECK_OK" if args.check else "HOMEPAGE_RENDER_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

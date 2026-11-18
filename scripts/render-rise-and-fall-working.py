#!/usr/bin/env python3
"""Refresh the non-frozen Rise & Fall HTML/PDF/EPUB projections from the book sources.

Source chapters are authoritative. Existing public HTML shells and navigation are
preserved; no immutable edition is modified. Requires markdown-it-py, Quarto's
pandoc, and Chromium (only for PDF rendering).
"""
from __future__ import annotations

import hashlib
import html
import os
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
import tempfile
from urllib.parse import urlsplit
from zipfile import ZipFile

from markdown_it import MarkdownIt
import yaml

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'projects/rise-and-fall'
SITE = PROJECT / 'site'
PROJECTIONS = PROJECT / 'projections'
REPO_URL = 'https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/'
MANUSCRIPT = PROJECT / 'manuscript/book'
CHAPTERS = (
    '00-ouverture.md', '01-methode-deux-passes.md',
    '02-antoine-dominique-et-titre-1813.md',
    '03-reality-case-rc01-1863.md', '04-reality-case-rc02-1924.md',
    '05-minesteggio-la-memoire-retrouve-un-nom.md',
    '06-deux-epoques-se-repondent.md', '07-chronologie-et-bifurcations.md',
    '08-questions-ouvertes.md',
)
MD = MarkdownIt('default', {'html': False, 'linkify': False, 'typographer': True}).enable('table')


def expect_replace(s: str, old: str, new: str, label: str) -> str:
    occurrences = s.count(old)
    if occurrences != 1:
        raise ValueError(f'{label}: expected one match, got {occurrences}')
    return s.replace(old, new)


def read_chapter(name: str) -> tuple[str, str]:
    value = (MANUSCRIPT / name).read_text('utf-8')
    m = re.match(r'\A---\s*\n.*?\n---\s*\n', value, flags=re.S)
    if not m:
        raise ValueError(f'missing frontmatter: {name}')
    body = value[m.end():].strip()
    first, sep, remainder = body.partition('\n')
    if not first.startswith('# ') or not sep:
        raise ValueError(f'missing title: {name}')
    return first[2:].strip(), remainder.strip() + '\n'


def render(name: str, body: str) -> str:
    rendered = MD.render(body)
    source = (Path('projects/rise-and-fall/manuscript/book') / name).parent
    def link_rewriter(match: re.Match[str]) -> str:
        attr = html.unescape(match.group(1))
        parts = urlsplit(attr)
        if parts.scheme or attr.startswith(('#', '/', '//', 'mailto:')):
            return match.group(0)
        target = posixpath.normpath(posixpath.join(str(source), parts.path))
        if target.startswith('..'):
            raise ValueError(f'link leaves repository: {attr}')
        url = REPO_URL + target
        if parts.fragment:
            url += '#' + parts.fragment
        return 'href="' + html.escape(url, quote=True) + '"'
    return re.sub(r'href="([^"]+)"', link_rewriter, rendered)


def replace_article(text: str, article_id: str, contents: str) -> str:
    pattern = re.compile(r'<article id="' + re.escape(article_id) + r'" class="chapter">.*?</article>', re.S)
    output, count = pattern.subn(lambda _m: contents, text)
    if count != 1:
        raise ValueError(f'{article_id}: {count} replacements')
    return output


def update_website(chapters: list[tuple[str, str, str]]) -> None:
    for filename in (SITE / 'book.html', PROJECTIONS / 'preview.html'):
        doc = filename.read_text('utf-8')
        for index, (name, title, body) in enumerate(chapters, start=1):
            article = (f'<article id="chapitre-{index}" class="chapter">\n'
                       f'  <header class="chapter-header"><p class="chapter-num">Chapitre {index}</p>'
                       f'<h2>{html.escape(title)}</h2></header>\n'
                       f'  <div class="chapter-content">\n{render(name, body)}  </div>\n'
                       f'</article>')
            doc = replace_article(doc, f'chapitre-{index}', article)
        doc = doc.replace(
            '<h3 style="margin-top:0;">Formats en préparation disponibles</h3>',
            '<h3 style="margin-top:0;">Formats de travail actualisés (non gelés)</h3>')
        doc = doc.replace(
            '    <a class="btn-download" href="../projections/preview.html"',
            '    <a class="btn-download" href="book.html"')
        doc = doc.replace('href="magazine.html">Magazine</a>', 'href="revolutions-lumineuses.html">Magazine</a>')
        doc = doc.replace('href="annexes.html">Annexes</a>',
            'href="https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/rise-and-fall/sources/README.md">Sources</a>')
        doc = doc.replace('href="mentions.html">Mentions</a>', 'href="mentions-legales.html">Mentions</a>')
        doc = doc.replace('href="book.html" target="_blank" style="background:#4a5568;">Version intégrale</a>',
            'href="editions/volume-1-preview/" target="_blank" style="background:#4a5568;">Préversion synthétique</a>')
        filename.write_text(doc, 'utf-8')

    preview = SITE / 'editions/volume-1-preview/index.html'
    doc = preview.read_text('utf-8')
    name, title, body = chapters[2]
    article = ('<article id="ch2" class="chapter">\n'
               '  <div class="chapter-meta">Chapitre 3 · Les Origines</div>\n'
               f'  <h2>{html.escape(title)}</h2>\n'
               f'  {render(name, body)}'
               '  <div class="back-to-top"><a href="#toc">&uarr; Retour à la table des matières</a></div>\n'
               '</article>')
    doc = replace_article(doc, 'ch2', article)
    doc = doc.replace('le titre westphalien de 1813', 'le titre westphalien (date à établir)')
    doc = doc.replace('titré baron westphalien en 1813', 'dont le titre baronal westphalien reste à dater précisément')
    preview.write_text(doc, 'utf-8')

    index = SITE / 'index.html'
    landing = index.read_text('utf-8')
    marker = '</div>\n\n<section id="genealogie">'
    note_link = REPO_URL + 'projects/rise-and-fall/investigation/notes/titre-mariani-legitimite-silences-et-branches.md'
    register_link = REPO_URL + 'projects/rise-and-fall/sources/README.md'
    update = (f'</div>\n\n<section id="etat-des-sources">\n'
              '<h2>État de l’enquête — novembre 2026</h2>\n'
              '<p>La concession baronale est attribuée à Jérôme Bonaparte par les sources historiques, '
              'mais la date de son acte primaire et ses règles de dévolution demeurent à établir. '
              'Les institutions françaises du Sceau ont connu des organisations successives '
              '(1808, 1814, 1859) ; l’absence d’homologation ne peut être conclue sans inventaire des fonds.</p>\n'
              f'<p><a href="{note_link}">Lire la note critique sur le titre et les deux branches</a> '
              f'· <a href="{register_link}">Consulter le registre des fonds archivistiques</a>.</p>\n'
              '</section>\n\n<section id="genealogie">')
    if 'id="etat-des-sources"' not in landing:
        landing = expect_replace(landing, marker, update, 'site-index')
    index.write_text(landing, 'utf-8')

    guide = SITE / 'guide.html'
    value = guide.read_text('utf-8')
    guide.write_text(value.replace('titre de baron westphalien conféré en 1813',
                                   'titre de baron westphalien dont la date reste à établir'), 'utf-8')
    llms = SITE / 'llms.txt'
    value = llms.read_text('utf-8')
    llms.write_text(value.replace('titre westphalien conféré en 1813 par le Roi Jérôme Bonaparte',
                                  'titre westphalien attribué au roi Jérôme Bonaparte, date de concession non établie'), 'utf-8')
    bootstrap = PROJECTIONS / 'book-bootstrap.yml'
    value = bootstrap.read_text('utf-8')
    bootstrap.write_text(value.replace('titre westphalien de 1813', 'titre westphalien (date à établir)'), 'utf-8')


def generate_formats(chapters: list[tuple[str, str, str]]) -> None:
    with tempfile.TemporaryDirectory(prefix='rise-fall-formats-') as d:
        tmp = Path(d)
        content = '# Rise & Fall of the Mariani Family\n\n*Volume I — 1776–1870. Projection de travail, non gelée.*\n\n'
        for _, title, body in chapters:
            content += f'\n# {title}\n\n' + body + '\n'
        md = tmp / 'book.md'
        md.write_text(content, 'utf-8')
        subprocess.run([
            'quarto', 'pandoc', str(md), '-f', 'markdown', '-t', 'epub3', '-s', '--toc',
            '--metadata', 'title=Rise & Fall of the Mariani Family — Volume I (travail)',
            '--metadata', 'author=Jean Hugues Noël Robert',
            '--metadata', 'lang=fr', '-o', str(SITE / 'book.epub'),
        ], check=True, timeout=70, capture_output=True)
        with ZipFile(SITE / 'book.epub') as archive:
            if archive.testzip() is not None or 'mimetype' not in archive.namelist():
                raise ValueError('EPUB invalid')
            data = b''.join(archive.read(i) for i in archive.namelist() if i.endswith(('.xhtml', '.html')))
            if b'1808' not in data or b'1859' not in data:
                raise ValueError('EPUB does not include corrected source')
        user_data = tmp / 'chrome'
        subprocess.run([
            'chromium', '--headless', '--no-sandbox', '--disable-gpu',
            '--disable-dev-shm-usage', '--disable-extensions', '--disable-background-networking',
            '--no-first-run', '--no-default-browser-check', '--no-pdf-header-footer',
            '--allow-file-access-from-files', '--user-data-dir=' + str(user_data),
            '--print-to-pdf=' + str(SITE / 'book.pdf'),
            (SITE / 'book.html').resolve().as_uri(),
        ], check=True, timeout=100, capture_output=True)
        pdf = (SITE / 'book.pdf').read_bytes()
        if not pdf.startswith(b'%PDF-') or b'%%EOF' not in pdf[-2048:]:
            raise ValueError('PDF failed validation')
    shutil.copy2(SITE / 'book.pdf', PROJECTIONS / 'preview.pdf')
    shutil.copy2(SITE / 'book.epub', PROJECTIONS / 'preview.epub')


def update_receipt() -> None:
    receipt = PROJECTIONS / 'preview.yml'
    data = yaml.safe_load(receipt.read_text('utf-8'))
    data['generated_at'] = '2026-11-18T18:00:00Z'
    for fmt, name in [('html', 'preview.html'), ('pdf', 'preview.pdf'), ('epub', 'preview.epub')]:
        raw = (PROJECTIONS / name).read_bytes()
        data['formats'][fmt]['sha256'] = hashlib.sha256(raw).hexdigest()
        data['formats'][fmt]['size'] = len(raw)
    receipt.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), 'utf-8')


def main() -> None:
    chapters = [(n, *read_chapter(n)) for n in CHAPTERS]
    update_website(chapters)
    generate_formats(chapters)
    update_receipt()
    new = (SITE / 'book.html').read_text('utf-8')
    preview = (SITE / 'editions/volume-1-preview/index.html').read_text('utf-8')
    for value in (new, preview):
        if 'Conseil du Sceau' not in value or '1808' not in value or '1859' not in value:
            raise ValueError('Corrections absent from a public HTML projection')
    for bad in ('signature de Jérôme Bonaparte dans la débâcle', 'titré baron westphalien en 1813',
                'n’a été institué qu’en 1859'):
        if bad in new or bad in preview:
            raise ValueError(f'obsolete claim in public projection: {bad}')
    print('RISE_FALL_WORKING_PROJECTIONS=PASS HTML=2 EPUB=1 PDF=1 PREVIEW=1')


if __name__ == '__main__':
    main()

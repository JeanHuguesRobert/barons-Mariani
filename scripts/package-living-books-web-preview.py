#!/usr/bin/env python3
"""Produce a self-contained static *working preview* from generated Markdown bundles.

No network or deployment operations. Deliberately conservative Markdown display:
the full source is HTML-escaped inside <pre>, never interpreted as trusted HTML.
"""
import hashlib
import html
import json
from pathlib import Path
import sys

def sha(data):
    return hashlib.sha256(data).hexdigest()

def package(input_dir: Path, output_dir: Path):
    meta = json.loads((input_dir / 'manifest.json').read_text(encoding='utf-8'))
    output_dir.mkdir(parents=True, exist_ok=True)
    pages = []
    for book in meta['books']:
        name = book['preview']
        source = input_dir / name
        raw = source.read_bytes()
        if sha(raw) != book['preview_sha256']:
            raise ValueError('Preview hash mismatch: ' + name)
        page = book['id'] + '.html'
        escaped = html.escape(raw.decode('utf-8'), quote=True)
        title = html.escape(book['id'])
        html_bytes = ('<!doctype html><html lang="fr"><meta charset="utf-8">'
                      '<meta name="viewport" content="width=device-width,initial-scale=1">'
                      '<meta name="robots" content="noindex,nofollow">'
                      '<title>EN PRÉPARATION — ' + title + '</title>'
                      '<style>body{font:1rem/1.5 system-ui;max-width:75ch;margin:2rem auto;padding:0 1rem}'
                      'pre{white-space:pre-wrap;overflow-wrap:anywhere}</style>'
                      '<nav><a href="index.html">Index des prévisualisations</a></nav>'
                      '<h1>EN PRÉPARATION — ' + title + '</h1>'
                      '<p>Document de travail, ni édition gelée ni publication canonique.</p>'
                      '<pre>' + escaped + '</pre></html>').encode('utf-8')
        (output_dir / page).write_bytes(html_bytes)
        pages.append({'book_id': book['id'], 'path': page, 'sha256': sha(html_bytes),
                      'input_sha256': sha(raw)})
    entries = ''.join('<li><a href="' + html.escape(p['path']) + '">' +
                      html.escape(p['book_id']) + '</a></li>' for p in pages)
    index = ('<!doctype html><html lang="fr"><meta charset="utf-8">'
             '<meta name="robots" content="noindex,nofollow"><title>Livres vivants — prévisualisations</title>'
             '<h1>Livres vivants — EN PRÉPARATION</h1>'
             '<p>Prévisualisations techniques non gelées et non canoniques.</p><ul>' +
             entries + '</ul></html>').encode('utf-8')
    (output_dir / 'index.html').write_bytes(index)
    record = {'schema': 'living-books.web-preview/v1', 'source_git_sha': meta['git_sha'],
              'status': 'working-unfrozen-not-published',
              'pages': pages, 'index_sha256': sha(index)}
    (output_dir / 'manifest.json').write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return record

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: package-living-books-web-preview.py INPUT_DIR OUTPUT_DIR')
    result = package(Path(sys.argv[1]), Path(sys.argv[2]))
    print('Packaged', len(result['pages']), 'static preview pages')

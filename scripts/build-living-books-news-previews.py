#!/usr/bin/env python3
"""Build non-frozen editorial previews; select books from declared dependencies."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'build' / 'living-books-news'
SOURCE = 'research/autonomia/observatoire_processus_autonomie_corse.md'
BOOKS = {
    'capable': 'projects/capable/editions/2026-10-09-en-preparation.md',
    'suicide-corse': 'projects/suicide-corse/editions/2026-10-09-n4-en-preparation.md',
    '1755': 'projects/1755/editions/2026-10-09-rc1-en-preparation.md',
}
SHARED_PATHS = {SOURCE, 'research/autonomia/courrier_rapporteur_senat_effectivite_72-5.md',
                'scripts/build-living-books-news-previews.py',
                '.github/workflows/living-books-news-previews.yml'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def impacted_books(paths):
    """Conservative dependency resolver: unknown inputs require review/full build."""
    paths = {p.strip().replace('\\', '/') for p in paths if p.strip()}
    if not paths or paths & SHARED_PATHS:
        return set(BOOKS)
    affected = set()
    unknown = []
    for path in paths:
        matched = False
        for book, edition in BOOKS.items():
            if path == edition or path.startswith(f'projects/{book}/'):
                affected.add(book)
                matched = True
        if not matched:
            unknown.append(path)
    if unknown:
        return set(BOOKS)  # fail open for correctness: unknown dependency, broad build
    return affected

def build(root, output, selected, commit='local'):
    source_bytes = (root / SOURCE).read_bytes()
    output.mkdir(parents=True, exist_ok=True)
    manifest = {
        'schema': 'living-books.news-preview/v1',
        'status': 'working-unfrozen-not-published',
        'source': SOURCE,
        'source_sha256': digest(source_bytes),
        'git_sha': commit,
        'built_at_utc': datetime.now(timezone.utc).isoformat(),
        'books': [],
    }
    for book in sorted(selected):
        src = BOOKS[book]
        data = (root / src).read_bytes()
        name = book + '-en-preparation.md'
        header = (f'# Aperçu documentaire — {book}\n\n'
                  '> **EN PRÉPARATION — non gelé, non publié comme édition.** '
                  'Ce paquet est une synthèse de provenance, non un livre rendu.\n\n'
                  f'Source : {SOURCE} (SHA-256: {digest(source_bytes)})\n\n'
                  f'État éditorial : {src} (SHA-256: {digest(data)})\n\n'
                  "Le contenu vérifié, les inconnues et les corrections appartiennent "
                  "à l'Observatoire et ne doivent pas être inventés ici.\n\n---\n\n")
        output_data = (header + data.decode('utf-8')).encode('utf-8')
        (output / name).write_bytes(output_data)
        manifest['books'].append({'id': book, 'input': src, 'sha256': digest(data),
                                  'preview': name, 'preview_sha256': digest(output_data)})
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return manifest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--book', action='append', choices=sorted(BOOKS), default=[])
    parser.add_argument('--changed-file', action='append', default=[])
    parser.add_argument('--changed-files-from', type=Path)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    files = args.changed_file[:]
    if args.changed_files_from:
        files.extend(args.changed_files_from.read_text(encoding='utf-8').splitlines())
    selected = set(args.book) if args.book else impacted_books(files)
    if args.dry_run:
        print(json.dumps({'selected_books': sorted(selected), 'changed_files': files}, ensure_ascii=False))
        return
    manifest = build(ROOT, OUT, selected, os.environ.get('GITHUB_SHA', 'local'))
    print('Built', len(manifest['books']), 'working previews:', OUT)

if __name__ == '__main__':
    main()

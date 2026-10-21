#!/usr/bin/env bash
# Preview only: do not email, publish, push or modify a serving release.
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
UBIKIA_DIR="${UBIKIA_DIR:-/srv/cogentia/repos/ubikia}"
SRC="$ROOT/research/senatoriales-2026/complement-2026-6589-sen"
STAGE="$(mktemp -d /tmp/sen-2026-6589-quarto-XXXXXX)"
echo "Staging: $STAGE"
command -v quarto
quarto --version
command -v node
test -f "$UBIKIA_DIR/package.json"
test -f "$SRC/projection-qpc-l299.yml"
test -f "$SRC/projection-qpc-l303.yml"
python3 "$ROOT/scripts/sen-2026-6589-build.py" --compose-only --out "$STAGE/composition"
# Generated intermediate: frontmatter is renderer-local, not a new sovereign source.
printf '%s\n' '---' 'title: "2026-6589 SEN — complément intégral"' 'language: fr' 'document_role: adapted' '---' > "$STAGE/consolidated.md"
cat "$STAGE/composition/complement-integral.preview.md" >> "$STAGE/consolidated.md"
cat > "$STAGE/corpus.yml" <<'EOF'
schema: ubikia.corpus.v0
project: 2026-6589 SEN
language: fr
source_root: .
sources:
  - path: consolidated.md
    role: derived-composite
    required: true
EOF
cat > "$STAGE/projection.yml" <<'EOF'
schema: ubikia.projection.book.v0
id: sen-2026-6589-consolidated-preview
status: working
language: fr
title: "2026-6589 SEN — complément intégral"
source_manifest: corpus.yml
chapters: [consolidated.md]
outputs:
  required: [pdf]
render_contract:
  canonical_source_format: markdown
  generated_qmd_is_source: false
  preserve_frontmatter_provenance: true
  preserve_epistemic_distinctions: true
  frozen_release_mutable: false
EOF
cd "$UBIKIA_DIR"
npm run render -- --corpus "$STAGE/corpus.yml" --projection "$STAGE/projection.yml" --output "$STAGE/render-consolidated"
npm run render -- --corpus "$SRC/corpus-ubikia.yml" --projection "$SRC/projection-qpc-l299.yml" --output "$STAGE/render-l299"
npm run render -- --corpus "$SRC/corpus-ubikia.yml" --projection "$SRC/projection-qpc-l303.yml" --output "$STAGE/render-l303"
echo "Inspect three Ubikia manifests and PDF outputs in: $STAGE"
echo "DRAFT ONLY — no transmission, deployment, or publication"

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
# Generate the plain-text projection from the identical composed Markdown.
# Quarto bundles Pandoc; no separate system Pandoc dependency.
quarto pandoc "$STAGE/composition/complement-integral.preview.md" \
  --from markdown --to plain --wrap=none \
  --output "$STAGE/courriel-integral.preview.txt"

# Fail closed on missing, empty, malformed, or unmanifested PDF outputs.
python3 - "$STAGE" "$ROOT" <<'PY'
import hashlib, json, pathlib, sys
stage, root = map(pathlib.Path, sys.argv[1:])
builds = ["render-consolidated", "render-l299", "render-l303"]
summary = {"status": "PREVIEW_ONLY_NOT_AUTHORIZED_TO_FILE", "source_git_manifest": str(stage / "composition" / "composition.preview.json"), "outputs": []}
for name in builds:
    folder = stage / name
    manifest_file = folder / "manifest.json"
    if not manifest_file.is_file():
        raise SystemExit(f"Missing Ubikia manifest: {manifest_file}")
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    pdfs = list(folder.rglob("*.pdf"))
    if len(pdfs) != 1:
        raise SystemExit(f"Expected exactly one PDF under {folder}, found {len(pdfs)}")
    pdf = pdfs[0]
    data = pdf.read_bytes()
    if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-2048:]:
        raise SystemExit(f"Malformed PDF: {pdf}")
    summary["outputs"].append({"role": name, "path": str(pdf), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "ubikia_manifest": str(manifest_file)})
txt = stage / "courriel-integral.preview.txt"
data = txt.read_bytes()
if not data.strip():
    raise SystemExit("Plain text is empty")
for token in [b"L.299", b"L.303"]:
    if token not in data:
        raise SystemExit(f"Missing QPC in plaintext: {token!r}")
summary["outputs"].append({"role": "mail-plaintext", "path": str(txt), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
out = stage / "delivery-preview-manifest.json"
out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(out)
PY
echo "Inspect three Ubikia manifests and PDF outputs in: $STAGE"
echo "DRAFT ONLY — no transmission, deployment, or publication"

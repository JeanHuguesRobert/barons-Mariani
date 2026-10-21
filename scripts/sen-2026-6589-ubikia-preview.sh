#!/usr/bin/env bash
# Preview only: do not email, publish, push or modify a serving release.
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
UBIKIA_DIR="${UBIKIA_DIR:-/srv/cogentia/repos/ubikia}"
SRC="$ROOT/research/senatoriales-2026/complement-2026-6589-sen"
if [[ -n "${SEN_PREVIEW_STAGE:-}" ]]; then
  STAGE="$SEN_PREVIEW_STAGE"
  mkdir "$STAGE"
else
  STAGE="$(mktemp -d /tmp/sen-2026-6589-quarto-XXXXXX)"
fi
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
npm run render -- --corpus "$STAGE/corpus.yml" --projection "$STAGE/projection.yml" --output "$STAGE/render-consolidated" 2>&1 | tee "$STAGE/render-consolidated.log"
npm run render -- --corpus "$SRC/corpus-ubikia.yml" --projection "$SRC/projection-qpc-l299.yml" --output "$STAGE/render-l299" 2>&1 | tee "$STAGE/render-l299.log"
npm run render -- --corpus "$SRC/corpus-ubikia.yml" --projection "$SRC/projection-qpc-l303.yml" --output "$STAGE/render-l303" 2>&1 | tee "$STAGE/render-l303.log"
# Generate the plain-text projection from the identical composed Markdown.
# Quarto bundles Pandoc; no separate system Pandoc dependency.
quarto pandoc "$STAGE/composition/complement-integral.preview.md" \
  --from markdown --to plain --wrap=none \
  --output "$STAGE/courriel-integral.preview.txt" 2>&1 | tee "$STAGE/render-plaintext.log"

# Fail closed on missing, empty, malformed, or unmanifested PDF outputs.
python3 - "$STAGE" "$ROOT" "$UBIKIA_DIR" <<'PY'
import hashlib, json, pathlib, subprocess, sys
stage, root = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
builds = ["render-consolidated", "render-l299", "render-l303"]
ubikia = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else None
def git_head(path):
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
summary = {
    "status": "build-preview",
    "filing_ready": False,
    "visual_review": "pending",
    "source_commit": git_head(root),
    "ubikia_commit": git_head(ubikia) if ubikia else None,
    "quarto_version": subprocess.check_output(["quarto", "--version"], text=True).strip(),
    "node_version": subprocess.check_output(["node", "--version"], text=True).strip(),
    "source_git_manifest": "composition/composition.preview.json",
    "outputs": [],
}
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
    manifest_bytes = manifest_file.read_bytes()
    summary["outputs"].append({"role": name, "path": str(pdf.relative_to(stage)), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "ubikia_manifest": str(manifest_file.relative_to(stage)), "ubikia_manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest()})
txt = stage / "courriel-integral.preview.txt"
data = txt.read_bytes()
if not data.strip():
    raise SystemExit("Plain text is empty")
for token in [b"L.299", b"L.303"]:
    if token not in data:
        raise SystemExit(f"Missing QPC in plaintext: {token!r}")
summary["outputs"].append({"role": "mail-plaintext", "path": str(txt.relative_to(stage)), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
out = stage / "delivery-preview-manifest.json"
out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(out)
PY
echo "Inspect three Ubikia manifests and PDF outputs in: $STAGE"
echo "DRAFT ONLY — no transmission, deployment, or publication"

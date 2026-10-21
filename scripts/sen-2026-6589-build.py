#!/usr/bin/env python3
"""Compile a reproducible *preview* from three Markdown sources and a selection contract.

Requirements: Python 3.10+, pandoc, and a working PDF engine (xelatex).
No network, upload, e-mail, signing, or filing is performed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEN = ROOT / "research" / "senatoriales-2026"
CON = SEN / "complement-2026-6589-sen"
MAIN = CON / "texte-maitre-travail-v0.1.md"
DELIVERY_SELECTION = CON / "delivery-selection.json"
L299 = SEN / "qpc" / "memoire-qpc-l299-formalisme-candidature-empechement-remplacant.md"
L303 = SEN / "qpc" / "memoire-qpc-l303-garanties-juridictionnelles.md"
FIRST = "## VI–VII. Mémoires QPC autonomes — inclusion par référence"
LAST = "## VIII. Bordereau et notes de provenance"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for data in iter(lambda: f.read(1 << 20), b""):
            h.update(data)
    return h.hexdigest()


def document(path: Path) -> str:
    value = path.read_text(encoding="utf-8")
    if not value.startswith("---\n"):
        raise ValueError(f"frontmatter missing in {path}")
    match = re.match(r"\A---\n.*?\n---\n", value, flags=re.S)
    if match is None:
        raise ValueError(f"frontmatter not closed in {path}")
    return value[match.end():].strip() + "\n"


def extract_qpc(path: Path) -> str:
    text = document(path)
    if "MÉMOIRE DISTINCT ET MOTIVÉ" not in text:
        raise ValueError(f"distinct memorandum heading missing: {path}")
    return text


def git_revision() -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()


def heading_span(text: str, heading: str) -> tuple[int, int]:
    matches = list(re.finditer(rf"(?m)^{re.escape(heading)}[ \t]*$", text))
    if len(matches) != 1:
        raise ValueError(f"delivery-selection heading must occur exactly once: {heading}")
    return matches[0].start(), matches[0].end()


def select_delivery_body(text: str) -> tuple[str, dict]:
    contract = json.loads(DELIVERY_SELECTION.read_text(encoding="utf-8"))
    if contract.get("source_path") != str(MAIN.relative_to(ROOT)):
        raise ValueError("delivery-selection source_path does not match the master document")
    title_start, title_end = heading_span(text, contract["title_heading"])
    body_start, _ = heading_span(text, contract["body_start_heading"])
    excluded_start, _ = heading_span(text, contract["exclude_from_heading"])
    if not title_start < title_end <= body_start < excluded_start:
        raise ValueError("delivery-selection headings are out of order")

    before_body = text[title_end:body_start].strip()
    after_body = text[excluded_start:].strip()
    selected = text[title_start:title_end].rstrip() + "\n\n" + text[body_start:excluded_start].strip() + "\n"
    for marker in contract.get("forbidden_output_markers", []):
        if marker in selected:
            raise ValueError(f"internal production marker remains in selected output: {marker}")

    exclusions = [
        {
            "id": "preparatory-notice-and-transmission-contract",
            "reason": contract["exclusion_reasons"]["before_body"],
            "bytes": len(before_body.encode("utf-8")),
            "sha256": hashlib.sha256(before_body.encode("utf-8")).hexdigest(),
        },
        {
            "id": "pre-emission-checklist",
            "reason": contract["exclusion_reasons"]["after_body"],
            "bytes": len(after_body.encode("utf-8")),
            "sha256": hashlib.sha256(after_body.encode("utf-8")).hexdigest(),
        },
    ]
    return selected, {
        "selection_id": contract["selection_id"],
        "source_path": contract["source_path"],
        "included_title_heading": contract["title_heading"],
        "included_from_heading": contract["body_start_heading"],
        "excluded_from_heading": contract["exclude_from_heading"],
        "purpose": contract["purpose"],
        "preserve_canonical_source": True,
        "excluded_ranges": exclusions,
    }


def make(out: Path, pdf_engine: str, compose_only: bool = False) -> None:
    main, delivery_selection = select_delivery_body(document(MAIN))
    q299 = extract_qpc(L299)
    q303 = extract_qpc(L303)
    if main.count(FIRST) != 1 or main.count(LAST) != 1:
        raise ValueError("ambiguous QPC slot anchors in main source")
    before, after_first = main.split(FIRST, 1)
    _, after = after_first.split(LAST, 1)
    # The QPC texts come only from their own sovereign source files.
    combined = before + "## VI. Mémoire distinct — QPC L.299\n\n" + q299 + "\n"
    combined += "## VII. Mémoire distinct — QPC L.303\n\n" + q303 + "\n"
    combined += LAST + after
    if combined.count("MÉMOIRE DISTINCT ET MOTIVÉ") < 2:
        raise ValueError("QPCs not fully included")
    out.mkdir(parents=True, exist_ok=True)
    md = out / "complement-integral.preview.md"
    md.write_text(combined, encoding="utf-8")
    source_pairs = [
        (MAIN, "consolidation"),
        (L299, "qpc-l299"),
        (L303, "qpc-l303"),
        (DELIVERY_SELECTION, "delivery-selection-contract"),
    ]
    manifest = {
        "purpose": "preview-only; not approved for filing",
        "source_git_commit": git_revision(),
        "delivery_selection": delivery_selection,
        "sources": [
            {"role": name, "path": str(path.relative_to(ROOT)), "sha256": sha256(path)}
            for path, name in source_pairs
        ],
        "outputs": [],
        "note": "Sending, receiving, registration and reading are distinct events."
    }
    if compose_only:
        (out / 'composition.preview.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(str(md))
        return
    # Pandoc produces plain UTF-8, not raw Markdown; no YAML in email body.
    commands = [
        (md, out / "courriel-integral.preview.txt", ["--to=plain", "--wrap=none"]),
        (md, out / "complement-integral.preview.pdf", ["--to=pdf", f"--pdf-engine={pdf_engine}", "--toc"]),
        (L299, out / "qpc-l299.preview.pdf", ["--to=pdf", f"--pdf-engine={pdf_engine}", "--toc"]),
        (L303, out / "qpc-l303.preview.pdf", ["--to=pdf", f"--pdf-engine={pdf_engine}", "--toc"])
    ]
    for source, target, opts in commands:
        cmd = ["pandoc", str(source), "--output", str(target), *opts]
        subprocess.run(cmd, check=True, cwd=ROOT)
        manifest["outputs"].append({
            "path": target.name,
            "bytes": target.stat().st_size,
            "sha256": sha256(target),
        })
    # Explicitly mark outputs as previews: legal/editorial audit still pending.
    (out / "manifest.preview.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="/tmp/sen-2026-6589-preview")
    parser.add_argument("--pdf-engine", default="xelatex")
    parser.add_argument("--compose-only", action="store_true")
    args = parser.parse_args()
    make(Path(args.out).resolve(), args.pdf_engine, args.compose_only)

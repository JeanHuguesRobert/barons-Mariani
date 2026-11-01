#!/usr/bin/env python3
"""FBF regression: exhibit communication must not silently become a new brief."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/sen-2026-6589-build.py"

with tempfile.TemporaryDirectory(prefix="sen-fbf-") as temp:
    root = Path(temp)
    subprocess.run([sys.executable, str(SCRIPT), "--compose-only", "--out", str(root / "exhibits")], check=True, capture_output=True, text=True)
    body = (root / "exhibits/communication-pieces.preview.md").read_text()
    manifest = json.loads((root / "exhibits/manifest.preview.json").read_text())
    assert "Communication des pièces citées" in body
    assert "## Notices prêtes à compléter" in body
    assert "MÉMOIRE DISTINCT ET MOTIVÉ" not in body
    assert "trois PDF joints" not in body
    assert manifest["mode"] == "exhibits" and manifest["filing_ready"] is False
    assert manifest["actual_attached_files"] == [] and manifest["sent"] is False
    assert not (root / "exhibits/complement-integral.preview.md").exists()
    subprocess.run([sys.executable, str(SCRIPT), "--compose-only", "--legacy-argumentative-preview", "--out", str(root / "legacy")], check=True, capture_output=True, text=True)
    legacy = (root / "legacy/complement-integral.preview.md").read_text()
    assert legacy.count("MÉMOIRE DISTINCT ET MOTIVÉ") >= 2
    assert not (root / "legacy/communication-pieces.preview.md").exists()
print("PASS FBF: default exhibits, explicit legacy QPC, no fictitious attachments")

#!/usr/bin/env python3
"""Nonprivileged integration smoke test for atomic Capable deployment."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[2]
DEPLOY = REPO / "scripts/ops/deploy-capable-working.py"


def run(revision, root, apply):
    command = [
        sys.executable, str(DEPLOY), "--revision", revision,
        "--repo", str(REPO), "--site-root", str(root), "--test-root",
    ]
    if apply:
        command += ["--apply"]
    r = subprocess.run(command, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-1500:])
    return json.loads(r.stdout)


def main():
    revision = subprocess.check_output(
        ["git", "-C", str(REPO), "rev-parse", "origin/main"], text=True,
    ).strip()
    # For CI, origin/main is the newest bot-published working source.
    # For local tests the caller should git fetch the remote first.
    with tempfile.TemporaryDirectory(prefix="capable-working-releases-") as td:
        root = Path(td)
        releases = root / "releases"
        releases.mkdir()
        prior = releases / "durable"
        prior.mkdir()
        (prior / "index.html").write_text(
            '<a href="en-preparation.html">le numéro en préparation</a>',
            encoding="utf-8",
        )
        original = b"FROZEN-AND-DURABLE-BOOK"
        for name in ("html", "pdf", "epub"):
            (prior / f"book.{name}").write_bytes(original + name.encode())
        (root / "current").symlink_to(Path("releases") / prior.name)
        dry = run(revision, root, False)
        assert dry["outcome"] == "DRY_RUN"
        new = run(revision, root, True)
        assert new["outcome"] == "DEPLOYED_VERIFIED"
        active = (root / "current").resolve()
        assert active.name == new["release"]
        assert active != prior
        for name in ("html", "pdf", "epub"):
            assert (prior / f"book.{name}").read_bytes() == original + name.encode()
            assert (active / f"book.{name}").read_bytes() == original + name.encode()
            assert (active / f"candidate.{name}").is_file()
        assert 'href="candidate.html"' in (
            active / "index.html"
        ).read_text(encoding="utf-8")
        assert "candidate.html" in (
            active / "en-preparation.html"
        ).read_text(encoding="utf-8")
        receipt = json.loads((active / "candidate-deploy.json").read_text())
        assert receipt["source_sha256"] == new["source_sha256"]
        assert len(list(releases.iterdir())) == 2
        again = run(revision, root, True)
        assert again["release"] == new["release"]
        assert len(list(releases.iterdir())) == 2
        assert (root / "current").resolve() == active
        print("CANONICAL_DEPLOY_TEST_PASS", new["release"],
              "source_count", new["input_count"], "idempotent", True)


if __name__ == "__main__":
    main()

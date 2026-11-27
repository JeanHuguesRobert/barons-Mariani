#!/usr/bin/env python3
"""Nonprivileged composition regression test, using an actual verified build."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile

spec = importlib.util.spec_from_file_location(
    "composition", Path(__file__).with_name("prepare-capable-composed-release.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def check(repo, revision, build, base):
    original = m.resource.inventory(base)
    with tempfile.TemporaryDirectory(prefix="capable-composition-test-") as td:
        root = Path(td)
        # Test against a copy; never alter production or the downloaded artifact.
        fixture = root / "base"
        shutil.copytree(base, fixture)
        copied = root / "build"
        shutil.copytree(build, copied)
        out = root / "out"
        out.mkdir()
        r = m.prepare(repo, revision, fixture, copied, out)
        assert r["outcome"] == "RELEASE_PREPARED", r
        candidate = out / r["release"]
        site = candidate / "site"
        actual = m.resource.inventory(site)
        assert actual == r["files"]
        assert m.resource.digest(m.resource.canonical(actual)) == r["tree_sha256"]
        public = json.loads((site / m.PUBLIC_RECEIPT).read_bytes())
        payload = {k: v for k, v in actual.items() if k != m.PUBLIC_RECEIPT}
        assert public["payload_tree_sha256"] == m.resource.digest(m.resource.canonical(payload))
        assert public["release"] == candidate.name
        assert public["resource_files"] == r["resource_files"]
        assert public["homepage_assets_sha256"]["index.html"] == actual["index.html"]["sha256"]
        assert public["annexes_page_sha256"] == actual["annexes.html"]["sha256"]
        assert "/ressources/index.html" in (site / "index.html").read_text()
        assert "/ressources/pacte-republicain-effectivite.html" in (site / "annexes.html").read_text()
        for name in ("book.html", "book.pdf", "book.epub"):
            assert original[name] == actual[name]
        assert all(original[n] == actual[n] for n in original if n.startswith("editions/"))
        again = m.prepare(repo, revision, site, copied, out, candidate / "receipt.json")
        assert again["outcome"] == "CURRENT_VERIFIED" and again["release"] == r["release"]
        # A corrupted transport must fail before preparing a release.
        bad = copied / "site/ressources/index.html"
        raw = bad.read_bytes()
        bad.write_bytes(raw + b"tamper")
        try:
            m.prepare(repo, revision, fixture, copied, out)
        except ValueError as error:
            assert "integrity mismatch" in str(error)
        else:
            raise AssertionError("Corrupted artifact accepted")
        bad.write_bytes(raw)
        # An inherited file changes the identity even if all generated files are identical.
        inherited = fixture / "robots.txt"
        inherited.write_bytes(inherited.read_bytes() + b"\n# inherited byte regression\n")
        changed = m.prepare(repo, revision, fixture, copied, out)
        assert changed["release"] != r["release"] and changed["tree_sha256"] != r["tree_sha256"]
        assert m.resource.inventory(base) == original
        print("CAPABLE_COMPOSED_REALITY_TEST_PASS", r["release"], r["tree_sha256"])


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--build", type=Path, required=True)
    p.add_argument("--base", type=Path, required=True,
                   help="Uncomposed working site fixture (read only)")
    a = p.parse_args()
    revision = m.resource.git(a.repo, "rev-parse", "origin/main").decode().strip()
    check(a.repo, revision, a.build, a.base)

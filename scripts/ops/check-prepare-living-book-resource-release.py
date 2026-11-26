#!/usr/bin/env python3
"""Reality test: prepare complete static resource releases without publication."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile

spec = importlib.util.spec_from_file_location("release", Path(__file__).with_name(
    "prepare-living-book-resource-release.py"))
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


def must_fail(action, contains):
    try:
        action()
    except ValueError as error:
        assert contains in str(error), str(error)
    else:
        raise AssertionError("Expected failure: " + contains)


with tempfile.TemporaryDirectory(prefix="resource-release-test-") as tmp:
    root = Path(tmp)
    repo, base, build, out = [root / name for name in ("repo", "base", "build", "out")]
    for d in (repo, base, build, out):
        d.mkdir()
    git = lambda *args: subprocess.check_output(["git", "-C", str(repo), *args],
                                               stderr=subprocess.DEVNULL).decode().strip()
    git("init", "-q")
    selection = repo / "projects/test/projections/resources-working.yml"
    selection.parent.mkdir(parents=True)
    selection.write_text("resources: test\n")
    source = repo / "source.md"
    source.write_text("public source\n")
    git("add", ".")
    git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "commit", "-qm", "Test")
    rev = git("rev-parse", "HEAD")
    git("update-ref", "refs/remotes/origin/main", rev)
    (base / "index.html").write_text('<nav><a href="/">Accueil</a></nav><h1>Test</h1>')
    (base / "sitemap.xml").write_text(
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '<url><loc>https://test.example/</loc></url>\n</urlset>\n')
    (base / "book.pdf").write_bytes(b"%PDF-unchanged")
    (base / "manifest.json").write_bytes(b'{"shared":true}')
    site = build / "site/ressources"
    site.mkdir(parents=True)
    (site / "index.html").write_text("Index")
    (site / "a.html").write_text("A")
    receipt = {
        "schema": "living-book.resource-projection/v1", "book_id": "test",
        "input_sha256": "input", "selection_revision": rev,
        "selection_sha256": release.digest(selection.read_bytes()),
        "resources": [{"id": "a", "route": "/ressources/a.html",
                       "source": "source.md", "source_revision": rev,
                       "sha256": release.digest(source.read_bytes())}],
        "artifacts": [{"route": "/" + p, **info}
                      for p, info in release.inventory(build / "site").items()]
    }
    (build / "receipt.json").write_bytes(release.canonical(receipt))
    before = release.inventory(base)
    prepare = lambda b=base, previous=None: release.prepare(
        repo, rev, "test", "test.example", b, build, out, previous)
    first = prepare()
    assert first == prepare()
    new = out / first["release"]
    assert release.inventory(base) == before
    assert release.inventory(new / "site") == first["files"]
    assert first["files"]["book.pdf"] == before["book.pdf"]
    assert first["files"]["manifest.json"] == before["manifest.json"]
    assert (new / "site/index.html").read_text().count(release.NAV) == 1
    assert (new / "site/sitemap.xml").read_text().count("https://test.example/ressources/a.html") == 1
    assert not (new / "site/receipt.json").exists()
    must_fail(lambda: prepare(new / "site"), "previous release receipt")
    before_count = len(list(out.iterdir()))
    unchanged = prepare(new / "site", new / "receipt.json")
    assert unchanged["tree_sha256"] == first["tree_sha256"]
    assert unchanged["outcome"] == "CURRENT_VERIFIED"
    assert len(list(out.iterdir())) == before_count
    (base / "manifest.json").write_bytes(b'{"shared":false}')
    second = prepare()
    assert second["tree_sha256"] != first["tree_sha256"]
    # Rebuild a changed resource, preserving prior owned namespace and all other bytes.
    (site / "a.html").write_text("A changed")
    receipt["artifacts"] = [{"route": "/" + p, **info}
                            for p, info in release.inventory(build / "site").items()]
    (build / "receipt.json").write_bytes(release.canonical(receipt))
    third = prepare(new / "site", new / "receipt.json")
    assert third["tree_sha256"] != first["tree_sha256"]
    assert third["files"]["book.pdf"] == first["files"]["book.pdf"]
    assert (out / third["release"] / "site/ressources/a.html").read_text() == "A changed"
    # A working site without a sitemap can be onboarded without
    # altering a frozen book or unrelated pages.
    (base / "sitemap.xml").unlink()
    (base / "index.html").write_text(
        '<link rel="canonical" href="https://test.example/">'
        '<nav><a href="/">Accueil</a></nav>')
    (base / "annexes.html").write_text(
        '<link rel="canonical" href="https://test.example/annexes.html">'
        '<a href="' + release.SOURCE_URL + 'source.md">Source</a>'
        '<a href="' + release.SOURCE_URL + 'other.md">Other</a>')
    before = release.inventory(base)
    fourth = release.prepare(repo, rev, "test", "test.example", base, build, out,
                             working_link_pages=("annexes.html",))
    fourth_dir = out / fourth["release"]
    assert release.inventory(base) == before
    assert fourth["files"]["book.pdf"] == before["book.pdf"]
    annexes = (fourth_dir / "site/annexes.html").read_text()
    assert 'href="/ressources/a.html">Source' in annexes
    assert release.SOURCE_URL + 'other.md' in annexes
    sitemap = (fourth_dir / "site/sitemap.xml").read_text()
    assert 'https://test.example/annexes.html' in sitemap
    assert 'https://test.example/ressources/a.html' in sitemap
    assert release.prepare(repo, rev, "test", "test.example",
        fourth_dir / "site", build, out, fourth_dir / "receipt.json",
        ("annexes.html",))["outcome"] == "CURRENT_VERIFIED"
    assert 'href="/ressources/new.html"' in release.project_working_links(
        annexes.encode(), {"source.md": "/ressources/new.html"},
        {"source.md": "/ressources/a.html"}).decode()
    assert release.SOURCE_URL + 'source.md' in release.project_working_links(
        annexes.encode(), {}, {"source.md": "/ressources/a.html"}).decode()
    (site / "a.html").write_text("tampered")
    must_fail(prepare, "integrity mismatch")
    (site / "a.html").write_text("A changed")
    (base / "symlink").symlink_to(source)
    must_fail(prepare, "Symlink")
    (base / "symlink").unlink()
    receipt["resources"][0]["sha256"] = "bad"
    (build / "receipt.json").write_bytes(release.canonical(receipt))
    must_fail(prepare, "Stale or uncommitted")
print("LIVING_BOOK_RESOURCE_RELEASE_REALITY_TEST_PASS")

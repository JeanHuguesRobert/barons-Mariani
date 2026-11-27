#!/usr/bin/env python3
"""Regression recovered from issue #112: escape, source hashes and repeatability."""
import importlib.util
import json
from pathlib import Path
import tempfile

source = Path(__file__).with_name("build-living-books-news-previews.py")
spec = importlib.util.spec_from_file_location("living_books_preview", source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# Distinct chapter and supporting research annexes.
capable = module.BOOKS["capable"]
assert 'projects/capable/manuscript/11-nouveau-contrat-social.md' in capable["chapters"]
for path in ['projects/capable/doctrine/nouveau-contrat-social.md', 'projects/capable/annexes/2026-11-27-college-interlocuteurs-nouveau-contrat-social.md', 'projects/capable/annexes/2026-11-27-minitelia-hypotheses-et-epreuves.md']:
    assert path in capable["annexes"] and path not in capable["chapters"]
with tempfile.TemporaryDirectory(prefix="living-books-recovered-test-") as temporary:
    root = Path(temporary)
    docs = root / "sample"
    docs.mkdir()
    (docs / "edition.md").write_text("# Plan de travail\n\nÉdition non gelée.\n", encoding="utf-8")
    original = "# Cas\n\n<script>alert('x')</script>\n\n[Plan](edition.md)\n"
    (docs / "chapter.md").write_text(original, encoding="utf-8")
    module.ROOT = root
    module.OUT = root / "previews"
    module.BOOKS = {"sample": {
        "edition": "sample/edition.md",
        "chapters": ["sample/chapter.md"],
    }}
    module.COMMON = []
    module.main()
    page = (module.OUT / "sample.html").read_text(encoding="utf-8")
    assert "&lt;script&gt;" in page and "<script>" not in page
    expected_anchor = module.source_anchor("sample/edition.md")
    assert ("href=\"#" + expected_anchor + "\"") in page
    record = json.loads((module.OUT / "manifest.json").read_text(encoding="utf-8"))
    assert record["status"] == "public-en-preparation-non-gele"
    files = ["sample.html", "manifest.json", "index.html"]
    first = {n: (module.OUT / n).read_bytes() for n in files}
    module.main()
    assert all((module.OUT / n).read_bytes() == first[n] for n in files)
    (docs / "chapter.md").write_text(original + "\nNouvel apport vérifiable.\n", encoding="utf-8")
    module.main()
    second = json.loads((module.OUT / "manifest.json").read_text(encoding="utf-8"))
    assert second["books"][0]["source_sha256"] != record["books"][0]["source_sha256"]
print("LIVING_BOOKS_PREVIEW_RECONCILIATION_PASS")

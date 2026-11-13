#!/usr/bin/env python3
"""FBF test: clean working-format reuse, and invalidation on damaged bytes."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "scripts/build-living-books-working-formats.py"
spec = importlib.util.spec_from_file_location("living_books_working_formats", ENTRY)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
real = ROOT / "previews/en-preparation"
manifest = json.loads((real / "manifest.json").read_text(encoding="utf-8"))
capable = next(x for x in manifest["books"] if x["id"] == "capable")
html = (real / "capable.html").read_text(encoding="utf-8")
with tempfile.TemporaryDirectory(prefix="living-book-formats-cache-") as td:
    module.OUT = Path(td)
    for name in ("capable.pdf", "capable.epub", "capable-formats.json"):
        shutil.copy2(real / name, module.OUT / name)
    assert module.reusable_receipt(capable, html) is not None
    damaged = module.OUT / "capable.pdf"
    damaged.write_bytes(damaged.read_bytes() + b"BAD-APPENDED-BY-TEST")
    assert module.reusable_receipt(capable, html) is None
    shutil.copy2(real / "capable.pdf", damaged)
    assert module.reusable_receipt(capable, html) is not None
    assert module.reusable_receipt(
        {**capable, "source_sha256": "0" * 64}, html) is None
    assert module.reusable_receipt(capable, html + "changed") is None
print("WORKING_FORMAT_CACHE_PASS: identical source reused, corruption/change invalidates")

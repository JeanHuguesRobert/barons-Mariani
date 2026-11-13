#!/usr/bin/env python3
"""Render existing Living Books working HTML into companion PDF and EPUB.

This is a format adapter for build-living-books-news-previews.py, not a
second manuscript compositor. It never touches frozen edition assets.
"""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from xml.etree import ElementTree as ET
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED, ZIP_STORED

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "previews" / "en-preparation"
MIMETYPE = b"application/epub+zip"
SOURCE = ROOT / "projects/capable/editions/2026-10-28-projection-candidate-n1.md"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def zipwrite(z, name, data, compression=ZIP_DEFLATED):
    meta = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
    meta.compress_type = compression
    z.writestr(meta, data)


def xhtml_from_preview(html):
    assert html.startswith("<!doctype html><html lang='fr'>")
    doc = html.replace("<!doctype html>", "", 1)
    doc = doc.replace(
        "<html lang='fr'>",
        "<html xmlns='http://www.w3.org/1999/xhtml' lang='fr' xml:lang='fr'>",
        1,
    )
    doc = doc.replace("<meta charset='utf-8'>", "<head><meta charset='utf-8' />", 1)
    doc = doc.replace(
        "<meta name='viewport' content='width=device-width'>",
        "<meta name='viewport' content='width=device-width' />",
        1,
    )
    doc = doc.replace("</style><body>", "</style></head><body>", 1)
    ET.fromstring(doc)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n' + doc).encode("utf-8")


def produce_epub(html, source_digest, date):
    xhtml = xhtml_from_preview(html)
    nav = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops" lang="fr">
<head><title>Sommaire — Capable, en préparation</title></head>
<body><nav epub:type="toc" id="toc">
<h1>Sommaire</h1>
<ol><li><a href="content.xhtml">Capable — édition de travail</a></li></ol>
</nav></body></html>""".encode("utf-8")
    modified = date + "T00:00:00Z"
    opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="fr">
 <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
  <dc:identifier id="pub-id">urn:sha256:{source_digest}</dc:identifier>
  <dc:title>Capable — premier numéro en préparation (non gelé)</dc:title>
  <dc:language>fr</dc:language>
  <dc:creator>Jean Hugues Noël Robert</dc:creator>
  <meta property="dcterms:modified">{modified}</meta>
 </metadata>
 <manifest>
  <item id="main" href="content.xhtml" media-type="application/xhtml+xml"/>
  <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
 </manifest>
 <spine><itemref idref="main"/></spine>
</package>""".encode("utf-8")
    container = b"""<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>"""
    for doc in (xhtml, nav, opf, container):
        ET.fromstring(doc)
    path = OUT / "capable.epub"
    with ZipFile(path, "w") as z:
        zipwrite(z, "mimetype", MIMETYPE, ZIP_STORED)
        zipwrite(z, "META-INF/container.xml", container)
        zipwrite(z, "OEBPS/content.opf", opf)
        zipwrite(z, "OEBPS/nav.xhtml", nav)
        zipwrite(z, "OEBPS/content.xhtml", xhtml)
    with ZipFile(path) as z:
        assert z.namelist()[0] == "mimetype"
        assert z.getinfo("mimetype").compress_type == ZIP_STORED
        assert z.testzip() is None
    return path


def produce_pdf():
    browser = next(
        (exe for name in ("chromium", "google-chrome", "chromium-browser")
         if (exe := shutil.which(name))),
        None,
    )
    if browser is None:
        raise RuntimeError("No Chromium/Chrome print engine installed for PDF preview")
    target = OUT / "capable.pdf"
    with tempfile.TemporaryDirectory(prefix="capable-render-") as user_data:
        cmd = [
            browser, "--headless", "--no-sandbox", "--disable-gpu",
            "--disable-dev-shm-usage", "--no-first-run",
            "--no-default-browser-check", "--disable-extensions",
            "--disable-background-networking", "--no-pdf-header-footer",
            "--user-data-dir=" + user_data,
            "--print-to-pdf=" + str(target),
            (OUT / "capable.html").resolve().as_uri(),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=70)
        if result.returncode:
            raise RuntimeError(f"PDF conversion failed (code {result.returncode}): "
                               + result.stderr[-1500:])
    raw = target.read_bytes()
    if not raw.startswith(b"%PDF-") or b"%%EOF" not in raw[-2048:]:
        raise ValueError("PDF preflight failed")
    return target


def main():
    manifest = json.loads((OUT / "manifest.json").read_text(encoding="utf-8"))
    item = next(book for book in manifest["books"] if book["id"] == "capable")
    html = (OUT / "capable.html").read_text(encoding="utf-8")
    if not all(s in html for s in (
        "PUBLIC · NON GELÉ",
        "Les collectivités territoriales ont droit aux adaptations",
        "Actualisation du 13 novembre 2026",
    )):
        raise ValueError("Existing HTML is not the expected 13-Nov Capable candidate")
    meta = SOURCE.read_text(encoding="utf-8")
    match = re.search(r'^last_modified_at:\s*["\']?(\d{4}-\d{2}-\d{2})', meta, re.M)
    if not match:
        raise ValueError("Working candidate must have last_modified_at")
    date = match.group(1)
    epub = produce_epub(html, item["source_sha256"], date)
    pdf = produce_pdf()
    receipt = {
        "schema": "living-books.working-formats/v1",
        "status": "en-preparation-non-gele",
        "source_sha256": item["source_sha256"],
        "inputs": len(item["inputs"]),
        "pdf": {"path": pdf.name, "sha256": digest(pdf.read_bytes()), "bytes": pdf.stat().st_size},
        "epub": {"path": epub.name, "sha256": digest(epub.read_bytes()), "bytes": epub.stat().st_size},
    }
    (OUT / "capable-formats.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == "__main__":
    main()

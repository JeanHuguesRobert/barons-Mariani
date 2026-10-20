#!/usr/bin/env python3
"""Diagnostic OCR only: printed-text OCR is unreliable on 18th-century handwriting."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

def run(image, output, lang="ita+fra"):
    image, output = Path(image), Path(output)
    output.mkdir(parents=True, exist_ok=True)
    data = image.read_bytes()
    # Use source image, not overlapping crops, to avoid duplicate recognized lines.
    proc = subprocess.run(["tesseract", str(image), "stdout", "-l", lang, "--psm", "3"],
                          capture_output=True, text=True, timeout=180, check=False)
    if proc.returncode:
        raise RuntimeError("Tesseract failed: " + proc.stderr[-1500:])
    raw = proc.stdout
    (output / "ocr-candidate.txt").write_text(raw, encoding="utf-8")
    metadata = {"schema":"scan-ocr-diagnostic/v1","image":image.name,
                "sha256":hashlib.sha256(data).hexdigest(),"engine":"tesseract",
                "language":lang,"page_segmentation_mode":3,
                "status":"machine-unreviewed","characters":len(raw),
                "warning":"Diagnostic only; handwritten text can be severely distorted. Not a transcription."}
    (output / "ocr-provenance.json").write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False))

if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("image")
    p.add_argument("--output",required=True)
    p.add_argument("--lang",default="ita+fra")
    a=p.parse_args()
    run(a.image,a.output,a.lang)

#!/usr/bin/env python3
"""Build an evidence context for the existing Cogentia continuation CLI.
This is NOT an independent Cognitive Packet protocol or lifecycle.
"""
import argparse
import hashlib
import json
from pathlib import Path

def build(manifest, diagnostic, ocr, image_ref, review_ref=None):
    m=json.loads(Path(manifest).read_text(encoding="utf-8"))
    d=json.loads(Path(diagnostic).read_text(encoding="utf-8"))
    raw=Path(ocr).read_bytes()
    if m["source_sha256"] != d["sha256"]:
        raise ValueError("Source digests disagree: refusing packet")
    if len(raw)>1_000_000:
        raise ValueError("OCR exceeds packet size limit")
    source=m["source_filename"]
    return {
      "schema":"scan-evidence-context/v1",
      "source":{"filename":source,"sha256":m["source_sha256"],"image_ref":image_ref,
                "dimensions":m["source_pixels"]},
      "evidence":{"crop_manifest":str(manifest),
                  "ocr_file":str(ocr),
                  "ocr_sha256":hashlib.sha256(raw).hexdigest(),
                  "ocr_diagnostic":str(diagnostic),
                  "ocr_engine":d["engine"],"ocr_language":d["language"],
                  "existing_reading_ref":review_ref},
      "judgment":{"required":"multimodal-paleographic-judgment",
                  "question":"Read a bounded zone directly from the scan, mark uncertainty, compare OCR only as a fallible hypothesis.",
                  "decision_options":["partial_reading","hold_for_tiff","reject_ocr","request_review"],
                  "must_preserve":["source_provenance","pixel_coordinates","contradictions","uncertainties"],
                  "publication_allowed":False},
      "status":"evidence_only_no_handler_claim"
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",required=True)
    p.add_argument("--diagnostic",required=True)
    p.add_argument("--ocr",required=True)
    p.add_argument("--image-ref",required=True)
    p.add_argument("--review-ref")
    p.add_argument("--output",required=True)
    a=p.parse_args()
    packet=build(a.manifest,a.diagnostic,a.ocr,a.image_ref,a.review_ref)
    Path(a.output).write_text(json.dumps(packet,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":"EVIDENCE_PREPARED","output":a.output,"image":a.image_ref}))
if __name__=="__main__":main()

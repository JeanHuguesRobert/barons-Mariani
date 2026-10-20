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
      "envelope":{
        "packet_kind":"continuation",
        "protocol_header":"Self-describing Cognitive Packet: resume the bounded work, verify evidence and write an auditable decision. Self-describing does not mean self-validating.",
        "profile":"scan-reading-judgment/v1",
        "transport":"referential",
        "provenance":{"source_sha256":m["source_sha256"],"source_filename":source,
                      "ocr_sha256":hashlib.sha256(raw).hexdigest(),
                      "ocr_engine":d["engine"],"ocr_language":d["language"]},
        "routing":{"required_capability":"multimodal-paleographic-judgment","state":"JUDGMENT_REQUIRED"}
      },
      "payload":{
        "question":"What characters, words, or lines in this image can be defended by direct visual reading? Identify contradictions with OCR and older editions without importing text silently.",
        "inputs":{
          "image":image_ref,
          "crop_manifest":str(manifest),
          "ocr_candidate":str(ocr),
          "ocr_diagnostic":str(diagnostic),
          "reference_reading":review_ref
        },
        "observations":["OCR is unreviewed and may be noise", "Source/crop fingerprints match the OCR source"],
        "unknown":["Accurate diplomatic line readings", "Page order and any restoration"],
        "next_action":"Inspect original image and targeted crops; read a bounded zone line-by-line; report observed/inferred/unknown and cite pixel coordinates.",
        "resume_contract":{
          "return_fields":["source_sha256","zone_box_xyxy","observed_lines","uncertain_readings","contradictions","evidence_refs","decision","next_action"],
          "allowed_decisions":["hold_for_tiff","partial_reading","reject_ocr","request_review"],
          "forbidden":["declare_verified_without_review","publish_unreviewed_ocr_as_manuscript_text","infer_missing_words_from_secondary_edition"]
        },
        "closure_status":"open",
        "publish_effect":"none"
      }
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
    print(json.dumps({"status":"JUDGMENT_REQUIRED","output":a.output,"image":a.image_ref}))
if __name__=="__main__":main()

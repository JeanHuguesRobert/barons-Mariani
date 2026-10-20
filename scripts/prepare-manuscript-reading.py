#!/usr/bin/env python3
"""Produce traceable reading crops from one archival image; never transcribe text."""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageOps

def prepare(source, destination, bands=4, overlap=120, margin=0, max_pixels=100_000_000):
    source, destination = Path(source), Path(destination)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    with Image.open(source) as original:
        width, height = original.size
        if width * height > max_pixels:
            raise ValueError("Image exceeds pixel safety limit")
        image = ImageOps.exif_transpose(original).convert("RGB")
    width, height = image.size
    if not 1 <= bands <= height:
        raise ValueError("bands must be between 1 and image height")
    if overlap < 0 or margin < 0 or margin * 2 >= width:
        raise ValueError("invalid overlap or margin")
    destination.mkdir(parents=True, exist_ok=True)
    stripe = (height + bands - 1) // bands
    records = []
    for index in range(bands):
        y0 = max(0, index * stripe - (overlap if index else 0))
        y1 = min(height, (index + 1) * stripe + (overlap if index + 1 < bands else 0))
        if y0 >= y1:
            continue
        box = (margin, y0, width - margin, y1)
        name = f"band-{index + 1:02d}.png"
        image.crop(box).save(destination / name, format="PNG")
        records.append({"file": name, "box_xyxy": list(box), "sha256": hashlib.sha256((destination / name).read_bytes()).hexdigest()})
    manifest = {
        "schema": "archival-reading-crops/v1",
        "source_filename": source.name,
        "source_sha256": digest,
        "source_pixels": [width, height],
        "transformation": "EXIF orientation normalized; RGB PNG; no OCR or transcription",
        "bands": bands, "overlap_px": overlap, "horizontal_margin_px": margin,
        "crops": records,
        "review_status": "unreviewed",
        "important": "Crops are aids for reading, not evidence of a verified text. Keep the source image."
    }
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("image", type=Path)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--bands", type=int, default=4)
    p.add_argument("--overlap", type=int, default=120)
    p.add_argument("--margin", type=int, default=0)
    args = p.parse_args()
    print(json.dumps(prepare(args.image, args.output, args.bands, args.overlap, args.margin), ensure_ascii=False))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""CI adapter: reuse Factory batch, bound cache, export verified public pages."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

BOOK = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
SHA = re.compile(r"[a-f0-9]{64}\Z")
REV = re.compile(r"[a-f0-9]{40}\Z")


def batch(path):
    data = json.loads(Path(path).read_bytes())
    if data["schema"] != "living-book.resource-batch/v1":
        raise ValueError("Invalid Factory batch schema")
    entries = {}
    for item in data["books"]:
        book, digest = item["book_id"], item["input_sha256"]
        if not BOOK.fullmatch(book) or not SHA.fullmatch(digest) or book in entries:
            raise ValueError("Invalid or duplicate book fingerprint")
        entries[book] = item
    return entries


def fingerprints(entries):
    return {book: item["input_sha256"] for book, item in sorted(entries.items())}


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()


def plan(path):
    return hashlib.sha256(canonical(fingerprints(batch(path)))).hexdigest()


def finish(plan_path, result_path, cache, output, corpus_revision, factory_revision):
    planned, actual = batch(plan_path), batch(result_path)
    if fingerprints(planned) != fingerprints(actual):
        raise ValueError("Inputs changed between plan and build")
    if not REV.fullmatch(corpus_revision) or not REV.fullmatch(factory_revision):
        raise ValueError("Invalid immutable revision")
    cache = Path(cache).resolve(strict=True)
    output = Path(output)
    if output.exists():
        raise ValueError("CI artifact directory must be new")
    keep, summary, sites = set(), [], []
    for book, item in sorted(actual.items()):
        if item["status"] not in ("BUILT_VERIFIED", "REUSED_VERIFIED"):
            raise ValueError("Factory did not verify build")
        directory = cache / (book + "-" + item["input_sha256"])
        if directory.is_symlink() or Path(item["directory"]).resolve() != directory:
            raise ValueError("Unexpected cache directory")
        keep.add(directory.name)
        receipt = json.loads((directory / "receipt.json").read_bytes())
        if receipt["book_id"] != book or receipt["input_sha256"] != item["input_sha256"]:
            raise ValueError("Unexpected Factory receipt")
        if not receipt.get("selection_revision") or any(
                not source.get("source_revision") for source in receipt["resources"]):
            raise ValueError("CI projections require committed source provenance")
        # Transport only the provenance required by the existing release
        # assembler. Editorial dispositions and unresolved links stay local.
        projected = {key: receipt[key] for key in (
            "schema", "book_id", "input_sha256", "implementation_sha256",
            "selection_sha256", "selection_revision", "resources", "artifacts")}
        raw = canonical(projected) + b"\n"
        summary.append({"book_id": book, "input_sha256": item["input_sha256"],
                        "status": item["status"], "artifacts": receipt["artifacts"],
                        "projection_receipt_sha256": hashlib.sha256(raw).hexdigest()})
        sites.append((book, directory / "site", raw))
    output.mkdir()
    for book, site, raw in sites:
        shutil.copytree(site, output / book / "site")
        (output / book / "receipt.json").write_bytes(raw)
    result = {"schema": "living-book.resource-ci/v2", "outcome": "BUILD_VERIFIED",
              "corpus_revision": corpus_revision, "factory_revision": factory_revision,
              "books": summary, "publication": "not_attempted"}
    (output / "build-receipt.json").write_bytes(canonical(result) + b"\n")
    # Only current selected fingerprints remain in the runner cache.
    # Older remote caches expire under the platform policy.
    for item in cache.iterdir():
        if item.name not in keep:
            if item.is_symlink() or not item.is_dir():
                raise ValueError("Unexpected entry in dedicated resource cache")
            shutil.rmtree(item)
    return result


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "plan":
        print("fingerprint=" + plan(sys.argv[2]))
    elif len(sys.argv) == 8 and sys.argv[1] == "finish":
        result = finish(*sys.argv[2:])
        print("## Resource projection build — no publication\n")
        for item in result["books"]:
            print(f"- {item['book_id']}: {item['status']} ({len(item['artifacts'])} files)")
    else:
        raise SystemExit("usage: plan PLAN | finish PLAN RESULT CACHE OUTPUT CORPUS_SHA FACTORY_SHA")

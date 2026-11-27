#!/usr/bin/env python3
"""Nonprivileged composition for the existing Capable deployment owner.

Consumes the verified canonical resource artifact and the legacy working
candidate through its existing reader. Does not install or switch current.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import tempfile


def sibling(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


resource = sibling("prepare-living-book-resource-release")
owner = sibling("deploy-capable-working")
transfer = sibling("prepare-living-book-ci-releases")
BOOK = "capable"
HOST = "capable.acorsica.org"
PUBLIC_RECEIPT = "candidate-deploy.json"


def working_layer(repo, revision):
    files, item, page, cases, magazine, annexes, guide, homepage = owner.read_candidate(repo, revision)
    payload = {
        "candidate.html": files["capable.html"], "candidate.pdf": files["capable.pdf"],
        "candidate.epub": files["capable.epub"], "candidate-manifest.json": files["manifest.json"],
        "candidate-formats.json": files["capable-formats.json"],
        "en-preparation.html": owner.localize_site_page(page).encode(),
        "cases.html": cases.encode(), "magazine.html": magazine.encode(),
        "annexes.html": annexes.encode(), **guide, **homepage}
    return payload, item, files


def public_receipt(site, item, files, resource_files, revision, previous_public):
    # A public receipt cannot include the digest of its own bytes. The public
    # release label identifies all payload files; the detached receipt below
    # covers the entire served tree, including this receipt.
    payload = resource.inventory(site)
    assert PUBLIC_RECEIPT not in payload
    label = "capable-work-" + resource.digest(resource.canonical(payload))
    sha = lambda name: payload[name]["sha256"]
    result = {
        "schema": "capable.canonical-working-deploy.v2",
        "status": "working-non-frozen", "revision": revision,
        "source_sha256": item["source_sha256"], "input_count": len(item["inputs"]),
        "durable_book_sha256": {n: sha(n) for n in ("book.html", "book.pdf", "book.epub")},
        "release": label, "payload_tree_sha256": label.removeprefix("capable-work-"),
        "case_page_sha256": sha("cases.html"), "magazine_page_sha256": sha("magazine.html"),
        "annexes_page_sha256": sha("annexes.html"),
        "guide_assets_sha256": {n: sha(n) for n in owner.GUIDE_ASSETS},
        "homepage_assets_sha256": {n: sha(n) for n in owner.HOMEPAGE_ASSETS},
        "files": {n: resource.digest(files[n]) for n in owner.PREVIEW},
        "resource_files": resource_files,
    }
    # Preserve creation provenance across unrelated commits, as the current owner does.
    if previous_public and owner.comparable_release_receipts(previous_public, result):
        return previous_public
    return result


def prepare(repo, revision, base, build, out, previous=None):
    if os.geteuid() == 0:
        raise ValueError("Preparation must remain nonprivileged")
    if not re.fullmatch(r"[0-9a-f]{40}", revision) or resource.git(
            repo, "rev-parse", "origin/main").decode().strip() != revision:
        raise ValueError("Expected current immutable origin/main revision")
    base, build, out = (p.resolve(strict=True) for p in (base, build, out))
    if any(out == p or p in out.parents for p in (base, build, repo.resolve(), Path("/srv/www"))):
        raise ValueError("Output must be outside the source, build and public trees")
    selected, projection_sha, resource_files = resource.verify_resource_build(repo, revision, BOOK, build)
    original = resource.inventory(base)
    old = json.loads(previous.read_bytes()) if previous else None
    if old and (old.get("files") != original or old.get("tree_sha256") !=
                resource.digest(resource.canonical(original)) or old.get("book_id") != BOOK):
        raise ValueError("Prior complete release differs from its receipt")
    prior_public = json.loads((base / PUBLIC_RECEIPT).read_bytes()) if PUBLIC_RECEIPT in original else None
    payload, item, preview = working_layer(repo, revision)
    work = Path(tempfile.mkdtemp(prefix=".capable-composed-", dir=out))
    try:
        site = work / "site"
        shutil.copytree(base, site)
        if resource.inventory(site) != original or resource.inventory(base) != original:
            raise ValueError("Base changed during staging")
        if (site / PUBLIC_RECEIPT).exists():
            (site / PUBLIC_RECEIPT).unlink()
        for name, data in payload.items():
            target = site / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        # Same resource planner and applicator as the eleven published books.
        _, old_resources, expected, changes, route_map = resource.resource_overlay_plan(
            site, BOOK, HOST, selected, resource_files, previous,
            ("annexes.html", "magazine.html"))
        resource.apply_resource_overlay(site, build, old_resources, expected, changes)
        for name, meta in original.items():
            if name != PUBLIC_RECEIPT and name not in payload and name not in changes and name not in old_resources:
                if expected.get(name) != meta:
                    raise ValueError("Inherited file changed: " + name)
        public = public_receipt(site, item, preview, resource_files, revision, prior_public)
        dest = out / public["release"]
        # If the same payload has already been prepared from another source
        # revision, reuse its creation receipt rather than changing its bytes.
        if dest.exists():
            if dest.is_symlink() or (dest / "site").is_symlink() or (dest / "site" / PUBLIC_RECEIPT).is_symlink():
                raise ValueError("Symlink in composed release")
            stored_public = json.loads((dest / "site" / PUBLIC_RECEIPT).read_bytes())
            if not owner.comparable_release_receipts(stored_public, public):
                raise ValueError("Existing payload receipt differs")
            public = stored_public
        (site / PUBLIC_RECEIPT).write_bytes(resource.canonical(public))
        complete = resource.inventory(site)
        tree = resource.digest(resource.canonical(complete))
        dest = out / public["release"]
        result = {
            "schema": "living-book.resource-release/v1", "book_id": BOOK,
            "canonical_host": HOST, "status": "working-non-frozen",
            "outcome": "RELEASE_PREPARED", "publication": "not_attempted",
            "deployment_owner": "capable canonical working deployer",
            "corpus_revision": revision, "resource_input_sha256": selected["input_sha256"],
            "resource_receipt_sha256": projection_sha,
            "base_tree_sha256": resource.digest(resource.canonical(original)),
            "payload_tree_sha256": public["payload_tree_sha256"],
            "tree_sha256": tree, "release": dest.name, "files": complete,
            "resource_files": resource_files, "working_link_routes": route_map,
        }
        if resource.inventory(base) != original:
            raise ValueError("Active base changed during preparation")
        if complete == original:
            result["outcome"] = "CURRENT_VERIFIED"
            return result
        if dest.exists():
            if dest.is_symlink() or resource.inventory(dest / "site") != complete:
                raise ValueError("Existing composed release differs")
            if (dest / "receipt.json").is_symlink():
                raise ValueError("Symlink in detached receipt")
            prior = json.loads((dest / "receipt.json").read_bytes())
            if (prior.get("files") != complete or prior.get("tree_sha256") != tree
                    or prior.get("release") != dest.name or prior.get("book_id") != BOOK):
                raise ValueError("Existing composed receipt differs")
            return prior
        (work / "receipt.json").write_bytes(resource.canonical(result))
        work.rename(dest)
        return result
    finally:
        if work.exists():
            shutil.rmtree(work)


def from_ci(repo, revision, artifact, run, base, out, previous=None):
    _, _, delivery = transfer.verify_transfer(repo, revision, artifact, run)
    result = prepare(repo, revision, base, artifact / BOOK, out, previous)
    return {**result, "delivery": delivery}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--run", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--previous-receipt", type=Path)
    args = parser.parse_args()
    import subprocess
    repo = args.repo.resolve(strict=True)
    revision = resource.git(repo, "rev-parse", "origin/main").decode().strip()
    run = json.loads(subprocess.check_output(["gh", "api", f"repos/{transfer.REPO}/actions/runs/{args.run}"]))
    transfer.verify_run(run, repo, revision)
    if run["id"] != args.run:
        raise ValueError("Unexpected run ID")
    current = Path("/srv/www/capable/current")
    base = current.resolve(strict=True)
    if not current.is_symlink() or base.parent != current.parent / "releases":
        raise ValueError("Unexpected Capable current layout")
    with transfer.receive_ci_artifact(run) as (artifact, transport):
        r = from_ci(repo, revision, artifact, run, base, args.out, args.previous_receipt)
        r["delivery"]["transport"] = transport
    if current.resolve() != base:
        raise ValueError("Current changed during composition")
    print(json.dumps(r, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

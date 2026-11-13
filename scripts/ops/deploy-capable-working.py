#!/usr/bin/env python3
"""Deploy Capable's non-frozen working edition into an immutable site release.

Source: verified origin/main Git objects, not the possibly dirty worktree.
Production execution requires the authorized host administrator; this file
does not confer privileges or modify frozen book.* artifacts.
"""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

DEFAULT_REPO = Path("/home/ubuntu/barons-Mariani")
DEFAULT_SITE = Path("/srv/www/capable")
PREFIX = "previews/en-preparation/"
PREVIEW = ("capable.html", "capable.pdf", "capable.epub",
           "capable-formats.json", "manifest.json")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(repo, revision, path):
    return subprocess.check_output(
        ["git", "-C", str(repo), "show", f"{revision}:{path}"],
        stderr=subprocess.DEVNULL,
    )


def read_candidate(repo, revision):
    files = {name: git_blob(repo, revision, PREFIX + name) for name in PREVIEW}
    manifest = json.loads(files["manifest.json"])
    receipt = json.loads(files["capable-formats.json"])
    item = next(book for book in manifest["books"] if book["id"] == "capable")
    expected = item["source_sha256"]
    if receipt["source_sha256"] != expected or len(item["inputs"]) < 20:
        raise ValueError("Candidate source count/digest mismatch")
    if receipt["status"] != "en-preparation-non-gele":
        raise ValueError("Candidate is not marked working/non-frozen")
    for source in item["inputs"]:
        actual = digest(git_blob(repo, revision, source["path"]))
        if actual != source["sha256"]:
            raise ValueError(f"Stale source in preview: {source['path']}")
    html = files["capable.html"].decode("utf-8")
    if not ("Les collectivités territoriales ont droit aux adaptations" in html
            and "13 novembre 2026" in html):
        raise ValueError("Article 72 candidate not found in HTML")
    opening = html.find("Livre — 00-ouverture")
    note = html.find("Note de composition du numéro")
    if opening < 0 or note <= opening:
        raise ValueError("Book opening must precede technical composition notes")
    if not files["capable.pdf"].startswith(b"%PDF-"):
        raise ValueError("Invalid PDF")
    if not files["capable.epub"].startswith(b"PK"):
        raise ValueError("Invalid EPUB")
    for kind in ("pdf", "epub"):
        meta = receipt[kind]
        data = files[f"capable.{kind}"]
        if meta["sha256"] != digest(data) or meta["bytes"] != len(data):
            raise ValueError(f"Receipt mismatch: {kind}")
    site_page = git_blob(
        repo, revision, "projects/capable/site/en-preparation.html"
    ).decode("utf-8")
    if "en préparation" not in site_page and "en-preparation" not in site_page:
        raise ValueError("Unexpected canonical working page")
    case_page = git_blob(
        repo, revision, "projects/capable/site/cases.html"
    ).decode("utf-8")
    if ('https://capable.acorsica.org/cases.html' not in case_page
            or "brouillons non relus" not in case_page
            or "case-05-dematerialisation" not in case_page):
        raise ValueError("Unexpected Case du Reel index page")
    return files, item, site_page, case_page


def new_homepage(old):
    marker = '<a href="en-preparation.html">le numéro en préparation</a>'
    if marker in old:
        old = old.replace(
            marker,
            '<a href="candidate.html">le Livre en préparation (HTML)</a> '
            '· <a href="candidate.pdf">PDF</a> '
            '· <a href="candidate.epub">EPUB</a>',
            1,
        )
    elif 'href="candidate.html"' not in old:
        raise ValueError("Cannot locate existing homepage working edition link")
    return old


def localize_site_page(page):
    external = ("https://jeanhuguesrobert.github.io/"
                "barons-Mariani/previews/en-preparation/capable.html")
    raw = ("https://raw.githubusercontent.com/JeanHuguesRobert/"
           "barons-Mariani/main/previews/en-preparation/")
    if external not in page:
        raise ValueError("Canonical source page lacks the working-HTML link")
    return (page.replace(external, "candidate.html")
                .replace(raw + "capable.pdf", "candidate.pdf")
                .replace(raw + "capable.epub", "candidate.epub"))



def comparable_release_receipts(previous, requested):
    """Allow only a changed source commit for an identical immutable release."""
    normalize = lambda receipt: {
        key: value for key, value in receipt.items() if key != "revision"
    }
    return normalize(previous) == normalize(requested)

def perform(repo, site_root, revision, apply):
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Revision must be an immutable 40-digit Git SHA")
    ref = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "origin/main"],
        text=True,
    ).strip()
    if ref != revision:
        raise ValueError("origin/main advanced; refresh and retry")
    files, item, site_page, case_page = read_candidate(repo, revision)
    resolved = site_root.resolve()
    releases = resolved / "releases"
    current = resolved / "current"
    if not current.is_symlink() or not releases.is_dir():
        raise ValueError("Expected immutable-release layout is missing")
    existing = current.resolve(strict=True)
    if existing.parent != releases:
        raise ValueError("Current release resolves outside releases directory")
    if not (existing / "book.html").is_file():
        raise ValueError("Current frozen/durable book is missing")
    base_home = (existing / "index.html").read_text(encoding="utf-8")
    new_home = new_homepage(base_home)
    new_page = localize_site_page(site_page)
    durable_hashes = {
        name: digest((existing / name).read_bytes())
        for name in ("book.html", "book.pdf", "book.epub")
    }
    version = digest(
        files["capable.html"] + files["capable.pdf"] +
        files["capable.epub"] + new_page.encode("utf-8") +
        case_page.encode("utf-8") + new_home.encode("utf-8") +
        "".join(durable_hashes.values()).encode("ascii")
    )[:16]
    dest = releases / f"capable-work-{version}"
    results = {
        "schema": "capable.canonical-working-deploy.v1",
        "status": "working-non-frozen",
        "revision": revision,
        "source_sha256": item["source_sha256"],
        "input_count": len(item["inputs"]),
        "durable_book_sha256": durable_hashes,
        "release": dest.name,
        "case_page_sha256": digest(case_page.encode("utf-8")),
        "files": {name: digest(files[name]) for name in PREVIEW},
    }
    if not apply:
        results["outcome"] = "DRY_RUN"
        return results

    # The lock is held through the copy, validation and atomic pointer swap.
    with open(resolved / ".capable-working-deploy.lock", "a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if dest.exists():
            stored = json.loads((dest / "candidate-deploy.json").read_text())
            # A later commit may change unrelated Corpus files without changing
            # a single deployed byte. The immutable release is content-addressed:
            # keep the original creation revision as provenance, rather than
            # rejecting an otherwise byte-identical deployment.
            if not comparable_release_receipts(stored, results):
                raise ValueError("Existing release differs from expected contents")
            results = dict(stored)
        else:
            staging = Path(tempfile.mkdtemp(prefix=".capable-work-", dir=releases))
            try:
                shutil.copytree(existing, staging, dirs_exist_ok=True)
                # Keep book.html/book.pdf/book.epub and dated editions exactly as served.
                for name in ("book.html", "book.pdf", "book.epub"):
                    if digest((staging / name).read_bytes()) != digest(
                        (existing / name).read_bytes()
                    ):
                        raise ValueError("Durable book changed during staging")
                (staging / "candidate.html").write_bytes(files["capable.html"])
                (staging / "candidate.pdf").write_bytes(files["capable.pdf"])
                (staging / "candidate.epub").write_bytes(files["capable.epub"])
                (staging / "candidate-manifest.json").write_bytes(files["manifest.json"])
                (staging / "candidate-formats.json").write_bytes(
                    files["capable-formats.json"]
                )
                (staging / "en-preparation.html").write_text(
                    new_page, encoding="utf-8"
                )
                (staging / "cases.html").write_text(
                    case_page, encoding="utf-8"
                )
                (staging / "index.html").write_text(new_home, encoding="utf-8")
                (staging / "candidate-deploy.json").write_text(
                    json.dumps(results, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8"
                )
                os.rename(staging, dest)
            finally:
                if staging.exists():
                    shutil.rmtree(staging)
        if current.resolve() != dest:
            temp_link = resolved / f".current-work-{os.getpid()}"
            try:
                temp_link.symlink_to(Path("releases") / dest.name)
                os.replace(temp_link, current)
            finally:
                if temp_link.is_symlink():
                    temp_link.unlink()
        if current.resolve() != dest:
            raise RuntimeError("Atomic release switch verification failed")
        results["outcome"] = "DEPLOYED_VERIFIED"
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    parser.add_argument("--site-root", type=Path, default=DEFAULT_SITE)
    parser.add_argument("--test-root", action="store_true",
                        help="Explicitly permit tests in a temporary site root")
    parser.add_argument("--apply", action="store_true",
                        help="Create immutable release and atomically switch current")
    args = parser.parse_args()
    if not args.test_root and args.site_root != DEFAULT_SITE:
        parser.error("Custom site root is only allowed with --test-root")
    # A trusted administrative executor must never accept test-root, a
    # caller-supplied Git repository, or an alternate production filesystem.
    if os.geteuid() == 0 and (
        args.test_root
        or args.repo != DEFAULT_REPO
        or args.site_root != DEFAULT_SITE
    ):
        parser.error("Root deployment is restricted to the canonical repo/site")
    try:
        result = perform(args.repo, args.site_root, args.revision, args.apply)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as error:
        print(f"DEPLOY_FAILED: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

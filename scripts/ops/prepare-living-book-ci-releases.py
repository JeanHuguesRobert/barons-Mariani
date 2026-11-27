#!/usr/bin/env python3
"""Consume a successful canonical CI run and prepare only changed site releases.

No root, no activation, no new renderer. Uses the existing release assembler.
The caller supplies the receipt of each already deployed resource release.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

spec = importlib.util.spec_from_file_location("release", Path(__file__).with_name(
    "prepare-living-book-resource-release.py"))
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)

REPO = "JeanHuguesRobert/barons-Mariani"
WORKFLOW = ".github/workflows/living-books-resources.yml"
SITES = {"1755": ("1755", "1755.acorsica.org"),
         "rise-and-fall": ("riseandfall", "riseandfall.baronsmariani.org"),
         "musee": ("musee", "museum.baronsmariani.org"),
         "school": ("school", "school.acorsica.org"),
         "commons": ("commons", "commons.acorsica.org"),
         "institut": ("institut", "institut.acorsica.org"),
         "privai": ("privai", "privai.acorsica.org"),
         "napoleon": ("napoleon", "napoleon.acorsica.org"),
         "village": ("village", "village.acorsica.org"),
         "diaspora": ("diaspora", "diaspora.acorsica.org"),
         "suicide-corse": ("suicidecorse", "suicidecorse.baronsmariani.org"),
         "orta": ("orta", "orta.acorsica.org"),
         "capable": ("capable", "capable.acorsica.org")}
WORKING_LINK_PAGES = {
    "musee": ("annexes.html", "magazine.html"),
    "commons": ("annexes.html", "sources.html", "magazine.html"),
    "institut": ("magazine.html",),
    "privai": ("annexes.html", "sources.html", "magazine.html"),
    "village": ("magazine.html",),
    "suicide-corse": ("index.html",),
}


# Local publication profiles. Rendering and resource URLs stay generic.
LAYOUTS = {
    "diaspora": {"home_page": "web/index.html", "entry_route": "/web/index.html"},
    "suicide-corse": {"navigation_container": "header"},
}
BOOTSTRAP = {"orta": "projects/orta/site"}
EXTERNAL_OWNER = {"capable": "existing canonical working deployer"}


def committed_site(repo, revision, prefix, destination):
    """Materialize only the explicitly declared committed site tree."""
    entries = release.git(repo, "ls-tree", "-r", "-z", revision, "--", prefix + "/")
    destination.mkdir()
    for entry in entries.split(b"\x00"):
        if not entry:
            continue
        metadata, name = entry.decode().split("\t", 1)
        mode, kind, _ = metadata.split(" ")
        if kind != "blob" or mode not in ("100644", "100755") or not name.startswith(prefix + "/"):
            raise ValueError("Unsupported bootstrap site entry")
        relative = name[len(prefix)+1:]
        path = Path(relative)
        if path.is_absolute() or any(part in ("", ".", "..") for part in relative.split("/")):
            raise ValueError("Unsafe bootstrap file")
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(release.git_bytes(repo, revision, name))
    if not (destination / "index.html").is_file():
        raise ValueError("Bootstrap site lacks committed homepage")


def pinned_factory(repo, revision):
    workflow = release.git_bytes(repo, revision, WORKFLOW).decode()
    pins = re.findall(r"repository: JeanHuguesRobert/cogentia\s+ref: ([a-f0-9]{40})\b", workflow)
    if len(pins) != 1:
        raise ValueError("Expected one pinned Factory revision")
    return pins[0]


def verify_run(run, revision):
    if (run.get("repository", {}).get("full_name") != REPO
            or run.get("head_repository", {}).get("full_name") != REPO
            or run.get("path") != WORKFLOW
            or run.get("head_branch") != "main"
            or run.get("head_sha") != revision
            or run.get("event") not in ("push", "workflow_dispatch")
            or run.get("status") != "completed"
            or run.get("conclusion") != "success"
            or not isinstance(run.get("id"), int)
            or not isinstance(run.get("run_attempt"), int)):
        raise ValueError("Expected successful canonical CI run for current origin/main")


def consume(repo, revision, artifact, out, previous_dir, webroot=Path("/srv/www")):
    receipt = json.loads((artifact / "build-receipt.json").read_bytes())
    if (receipt.get("schema") != "living-book.resource-ci/v2"
            or receipt.get("outcome") != "BUILD_VERIFIED"
            or receipt.get("publication") != "not_attempted"
            or receipt.get("corpus_revision") != revision
            or receipt.get("factory_revision") != pinned_factory(repo, revision)):
        raise ValueError("CI receipt revision or contract mismatch")
    books = receipt["books"]
    ids = [item["book_id"] for item in books]
    if len(ids) != len(set(ids)) or set(ids) != set(SITES):
        raise ValueError("Unexpected books in pilot CI artifact")
    expected_entries = {"build-receipt.json", *ids}
    if {p.name for p in artifact.iterdir()} != expected_entries:
        raise ValueError("Unexpected artifact entries")
    plans, results = [], []
    # Verify the whole transfer before assembling any candidate.
    for item in books:
        book = item["book_id"]
        if item["status"] not in ("BUILT_VERIFIED", "REUSED_VERIFIED"):
            raise ValueError("Unverified CI artifact")
        build = artifact / book
        if build.is_symlink() or {p.name for p in build.iterdir()} != {"site", "receipt.json"}:
            raise ValueError("Unexpected projection build entries")
        pr, digest, _ = release.verify_resource_build(repo, revision, book, build)
        if (digest != item["projection_receipt_sha256"]
                or pr["input_sha256"] != item["input_sha256"]
                or pr["artifacts"] != item["artifacts"]):
            raise ValueError("CI-to-projection receipt mismatch")
        slug, host = SITES[book]
        if book in EXTERNAL_OWNER:
            results.append({"book_id": book, "canonical_host": host,
                "outcome": "BUILD_VERIFIED_EXTERNAL_OWNER",
                "deployment_owner": EXTERNAL_OWNER[book],
                "resource_input_sha256": pr["input_sha256"],
                "resource_files": {x["route"][1:]: {"sha256": x["sha256"], "size": x["size"]}
                                   for x in pr["artifacts"]}})
            continue
        current = webroot / slug / "current"
        if not current.exists() and not current.is_symlink() and book in BOOTSTRAP:
            plans.append((book, host, current, None, build, None))
            continue
        if not current.is_symlink() or current.resolve().parent != (webroot / slug / "releases").resolve():
            raise ValueError("Unexpected current release layout")
        base = current.resolve(strict=True)
        previous = previous_dir / base.name / "receipt.json"
        if (base / "ressources").exists():
            if not previous.is_file() or previous.is_symlink():
                raise ValueError("Missing previous resource release receipt: " + book)
            old = json.loads(previous.read_bytes())
            # On the initial pilot and later immutable releases, the actual
            # current release must agree with its recorded complete manifest.
            if (old.get("release") != base.name
                    or old.get("tree_sha256") != release.digest(release.canonical(old["files"]))
                    or base.name != book + "-resources-" + old["tree_sha256"]
                    or release.inventory(base) != old["files"]):
                raise ValueError("Previous immutable release differs from receipt: " + book)
        else:
            previous = None
        plans.append((book, host, current, base, build, previous))
    for book, host, current, base, build, previous in plans:
        if base is None:
            with tempfile.TemporaryDirectory(prefix="living-book-bootstrap-") as tmp:
                staged = Path(tmp) / "site"
                committed_site(repo, revision, BOOTSTRAP[book], staged)
                r = release.prepare(repo, revision, book, host, staged, build, out,
                                    working_link_pages=WORKING_LINK_PAGES.get(book, ()),
                                    **LAYOUTS.get(book, {}))
            if current.exists() or current.is_symlink():
                raise ValueError("Current appeared during bootstrap: " + book)
            r = {**r, "outcome": "BOOTSTRAP_PREPARED", "publication": "origin_not_provisioned"}
        else:
            r = release.prepare(repo, revision, book, host, base, build, out, previous,
                                WORKING_LINK_PAGES.get(book, ()), **LAYOUTS.get(book, {}))
            if current.resolve() != base:
                raise ValueError("Current changed during assembly: " + book)
        results.append(r)
    results.sort(key=lambda r: r["book_id"])
    return {"schema": "living-book.resource-cd-preparation/v1",
            "corpus_revision": revision, "factory_revision": receipt["factory_revision"],
            "publication": "not_attempted", "books": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--run", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--previous-receipts", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve(strict=True)
    revision = release.git(repo, "rev-parse", "origin/main").decode().strip()
    run = json.loads(subprocess.check_output(
        ["gh", "api", f"repos/{REPO}/actions/runs/{args.run}"]))
    verify_run(run, revision)
    if run["id"] != args.run:
        raise ValueError("Unexpected run ID")
    name = f"living-books-resource-build-{args.run}-{run['run_attempt']}"
    with tempfile.TemporaryDirectory(prefix="living-book-ci-transfer-") as tmp:
        subprocess.run(["gh", "run", "download", str(args.run), "--repo", REPO,
                        "--name", name, "--dir", tmp], check=True)
        result = consume(repo, revision, Path(tmp), args.out,
                         args.previous_receipts.resolve(strict=True))
    result["ci_run_id"] = args.run
    result["ci_run_attempt"] = run["run_attempt"]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

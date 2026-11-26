#!/usr/bin/env python3
"""Compose a non-public, content-addressed Living Book resource release.

Preserves the existing site, including durable editions. The output consists
of a site tree and a separate receipt. It neither installs nor activates it.
"""
import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from xml.etree import ElementTree as ET

ROUTE = re.compile(r"/ressources/[a-z0-9][a-z0-9-]*\.html\Z")
BOOK = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
HOST = re.compile(r"[a-z0-9][a-z0-9.-]*\.[a-z]{2,}\Z")
INDEX = "/ressources/index.html"
NAV = '<a data-lbf-resources="true" href="/ressources/index.html">Ressources documentaires</a>'
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
            + "\n").encode()


def inventory(root):
    """Every public regular file, including inherited assets and manifests."""
    result = {}
    for file in sorted(root.rglob("*")):
        if file.is_symlink():
            raise ValueError(f"Symlink in public tree: {file}")
        if file.is_dir():
            continue
        if not file.is_file():
            raise ValueError(f"Not a regular file: {file}")
        data = file.read_bytes()
        result[file.relative_to(root).as_posix()] = {
            "sha256": digest(data), "size": len(data)}
    return result


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args],
                                   stderr=subprocess.DEVNULL)


def git_bytes(repo, revision, source):
    if not isinstance(source, str) or any(part in ("", ".", "..")
            for part in source.split("/")) or "\\" in source or ":" in source:
        raise ValueError("Unsafe Corpus path")
    return git(repo, "show", f"{revision}:{source}")


def verify_resource_build(repo, revision, book, build):
    receipt_file = build / "receipt.json"
    site = build / "site"
    if receipt_file.is_symlink() or site.is_symlink():
        raise ValueError("Symlink in resource build")
    raw = receipt_file.read_bytes()
    receipt = json.loads(raw)
    if receipt["schema"] != "living-book.resource-projection/v1" or receipt["book_id"] != book:
        raise ValueError("Resource receipt belongs to another book")
    if not receipt.get("input_sha256") or not receipt.get("selection_revision"):
        raise ValueError("Resource build must be committed and attributable")
    selection = f"projects/{book}/projections/resources-working.yml"
    if digest(git_bytes(repo, revision, selection)) != receipt["selection_sha256"]:
        raise ValueError("Resource selection is stale")
    for source in receipt["resources"]:
        if not source.get("source_revision") or digest(
                git_bytes(repo, revision, source["source"])) != source["sha256"]:
            raise ValueError(f"Stale or uncommitted selected source: {source['id']}")
    routes = [item["route"] for item in receipt["resources"]] + [INDEX]
    if len(routes) != len(set(routes)) or any(not ROUTE.fullmatch(route) for route in routes):
        raise ValueError("Invalid resource route map")
    expected = {}
    for item in receipt["artifacts"]:
        route = item["route"]
        if route not in routes or route[1:] in expected:
            raise ValueError("Invalid resource artifact route")
        expected[route[1:]] = {"sha256": item["sha256"], "size": item["size"]}
    if set(expected) != {route[1:] for route in routes} or inventory(site) != expected:
        raise ValueError("Resource artifact integrity mismatch")
    return receipt, digest(raw), expected


def add_navigation(data):
    text = data.decode("utf-8")
    if NAV in text:
        if text.count(NAV) != 1:
            raise ValueError("Duplicate resource navigation")
        return data
    if 'data-lbf-resources=' in text or '/ressources/index.html' in text:
        raise ValueError("Unrecognized existing resource navigation")
    match = re.search(r"<nav\b[^>]*>[\s\S]*?</nav\s*>", text, re.I)
    if not match:
        raise ValueError("Homepage lacks navigation")
    end = text.lower().rfind("</nav", match.start(), match.end())
    return (text[:end] + "  " + NAV + "\n" + text[end:]).encode()


def add_sitemap(data, host, routes, previous_routes=()):
    text = data.decode("utf-8")
    for route in previous_routes:
        entry = f"  <url><loc>https://{host}{route}</loc></url>\n"
        if text.count(entry) != 1:
            raise ValueError("Previous generated sitemap entry missing or duplicated")
        text = text.replace(entry, "", 1)
    before = ET.fromstring(text)
    if before.tag != SITEMAP_NS + "urlset":
        raise ValueError("Unexpected sitemap format")
    locations = [node.text for node in before.findall(".//" + SITEMAP_NS + "loc")]
    if len(locations) != len(set(locations)) or not any(
            url and url.startswith(f"https://{host}/") for url in locations):
        raise ValueError("Unexpected or duplicate sitemap URLs")
    generated = [f"https://{host}{route}" for route in sorted(routes)]
    if set(locations).intersection(generated):
        raise ValueError("Resource URL already present without ownership receipt")
    closing = text.rfind("</urlset>")
    if closing < 0:
        raise ValueError("Missing sitemap closing element")
    entries = "".join(f"  <url><loc>{escape(url)}</loc></url>\n" for url in generated)
    result = (text[:closing] + entries + text[closing:]).encode()
    actual = [node.text for node in ET.fromstring(result).findall(".//" + SITEMAP_NS + "loc")]
    if sorted(actual) != sorted(locations + generated):
        raise ValueError("Sitemap validation failed")
    return result


SOURCE_URL = "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/"


def initial_sitemap(base, host):
    """Only canonical root-level pages actually present, not guessed URLs."""
    locations = []
    for file in sorted(base.glob("*.html")):
        text = file.read_text()
        matches = re.findall(r'<link\s+rel="canonical"\s+href="([^"]+)"', text)
        url = f"https://{host}/" + ("" if file.name == "index.html" else file.name)
        if matches == [url]:
            locations.append(url)
    if f"https://{host}/" not in locations:
        raise ValueError("Homepage canonical URL required for initial sitemap")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{escape(url)}</loc></url>\n" for url in locations)
            + "</urlset>\n").encode()


def project_working_links(data, route_map, previous_map):
    """Rewrite exact anchor hrefs only; preserve all unrelated bytes.

    Restore the canonical source link if an earlier managed route is removed.
    """
    reverse = {route: SOURCE_URL + source for source, route in previous_map.items()}
    def replace(match):
        href = match[2]
        original = reverse.get(href, href)
        if original.startswith(SOURCE_URL):
            original = route_map.get(original[len(SOURCE_URL):], original)
        return match[1] + original + '"'
    return re.sub(r'(<a\b[^>]*?\bhref=")([^"]*)"', replace, data.decode(), flags=re.I).encode()


def prepare(repo, revision, book, host, base, build, out, previous=None, working_link_pages=()):
    if not BOOK.fullmatch(book) or not HOST.fullmatch(host):
        raise ValueError("Invalid book or canonical host")
    if not re.fullmatch(r"[0-9a-f]{40}", revision) or git(
            repo, "rev-parse", "origin/main").decode().strip() != revision:
        raise ValueError("Expected current immutable origin/main revision")
    base = base.resolve(strict=True)
    build = build.resolve(strict=True)
    out = out.resolve(strict=True)
    # Output is a local build directory, not a deployment destination.
    if any(out == p or p in out.parents for p in (base, build, repo.resolve(), Path("/srv/www"))):
        raise ValueError("Release output must be outside source/build/public trees")
    receipt, receipt_sha, resource_files = verify_resource_build(repo, revision, book, build)
    inherited = inventory(base)
    if "index.html" not in inherited:
        raise ValueError("Existing site lacks homepage")
    old = {}
    old_resources = {k: v for k, v in inherited.items() if k.startswith("ressources/")}
    if (base / "ressources").exists():
        if not old_resources:
            raise ValueError("Unowned empty resource namespace")
        if previous is None:
            raise ValueError("Existing resource namespace requires its previous release receipt")
        old = json.loads(previous.read_bytes())
        if (old.get("schema") != "living-book.resource-release/v1"
                or old.get("book_id") != book or old.get("canonical_host") != host
                or old.get("resource_files") != old_resources):
            raise ValueError("Existing resource namespace differs from prior receipt")
    elif previous is not None:
        raise ValueError("Previous resource receipt without existing resources")
    homepage = add_navigation((base / "index.html").read_bytes())
    sitemap_base = ((base / "sitemap.xml").read_bytes() if "sitemap.xml" in inherited
                    else initial_sitemap(base, host))
    sitemap = add_sitemap(sitemap_base, host,
                          ["/" + name for name in resource_files],
                          ["/" + name for name in old_resources])
    expected = {name: info for name, info in inherited.items() if name not in old_resources}
    expected.update(resource_files)
    changes = {"index.html": homepage, "sitemap.xml": sitemap}
    route_map = {item["source"]: item["route"] for item in receipt["resources"]}
    previous_map = old.get("working_link_routes", {})
    for name in working_link_pages:
        if not re.fullmatch(r"[a-z0-9-]+\.html", name) or name not in inherited or name == "index.html":
            raise ValueError("Invalid explicitly managed working link page")
        changes[name] = project_working_links((base / name).read_bytes(), route_map, previous_map)
    for name, content in changes.items():
        expected[name] = {"sha256": digest(content), "size": len(content)}
    tree_sha = digest(canonical(expected))
    dest = out / f"{book}-resources-{tree_sha}"
    result = {
        "schema": "living-book.resource-release/v1",
        "book_id": book, "canonical_host": host,
        "status": "working-non-frozen", "outcome": "RELEASE_PREPARED",
        "corpus_revision": revision,
        "resource_input_sha256": receipt["input_sha256"],
        "resource_receipt_sha256": receipt_sha,
        "base_tree_sha256": digest(canonical(inherited)),
        "tree_sha256": tree_sha, "release": dest.name,
        "resource_files": resource_files, "files": expected,
        "working_link_routes": route_map if working_link_pages else {},
    }
    # Do not create a duplicate release when the current site already serves
    # exactly the requested bytes. Verify ownership and all inputs above first.
    if expected == inherited:
        result["outcome"] = "CURRENT_VERIFIED"
        return result
    # Keep provenance and operational metadata outside the public document root.
    # Identical deployed bytes have identical identity, independent of unrelated commits.
    if dest.exists():
        if dest.is_symlink() or (dest / "site").is_symlink() or inventory(dest / "site") != expected:
            raise ValueError("Existing release integrity mismatch")
        if (dest / "receipt.json").is_symlink():
            raise ValueError("Symlink in existing release receipt")
        stored = json.loads((dest / "receipt.json").read_bytes())
        if (stored.get("tree_sha256") != tree_sha or stored.get("files") != expected
                or stored.get("book_id") != book or stored.get("canonical_host") != host):
            raise ValueError("Existing release receipt mismatch")
        # The release is immutable; preserve its original creation receipt.
        # A subsequent build with unchanged served bytes is a reuse, not a
        # replacement of that historical receipt.
        return stored
    staging = Path(tempfile.mkdtemp(prefix=".resource-release-", dir=out))
    try:
        site = staging / "site"
        shutil.copytree(base, site, symlinks=True)
        if inventory(site) != inherited or inventory(base) != inherited:
            raise ValueError("Base changed during release assembly")
        if old_resources:
            shutil.rmtree(site / "ressources")
        shutil.copytree(build / "site" / "ressources", site / "ressources")
        for name, content in changes.items():
            (site / name).write_bytes(content)
        if inventory(site) != expected:
            raise ValueError("Assembled release differs from complete byte manifest")
        (staging / "receipt.json").write_bytes(canonical(result))
        staging.rename(dest)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--book", required=True)
    parser.add_argument("--host", required=True)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--previous-receipt", type=Path)
    parser.add_argument("--working-link-page", action="append", default=[])
    args = parser.parse_args()
    result = prepare(args.repo, args.revision, args.book, args.host, args.base,
                     args.build, args.out, args.previous_receipt, args.working_link_page)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Test artifact identity, transport integrity and bounded ZIP extraction."""
import hashlib
import importlib.util
from pathlib import Path
import stat
import tempfile
import warnings
import zipfile

spec = importlib.util.spec_from_file_location(
    "transfer", Path(__file__).with_name("prepare-living-book-ci-releases.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def reject(fn, message):
    try:
        fn()
    except ValueError as error:
        assert message in str(error), error
    else:
        raise AssertionError("Expected rejection: " + message)


def check(root):
    run = {"id": 123, "run_attempt": 2, "head_sha": "a" * 40,
           "repository": {"id": 456}, "head_repository": {"id": 456}}
    linked = {"id": 123, "head_branch": "main", "head_sha": run["head_sha"],
              "repository_id": 456, "head_repository_id": 456}
    archive = root / "parcel.zip"

    def create(extra=(), omit=None):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(archive, "w") as z:
                for path in ["build-receipt.json", *(
                        f"{b}/receipt.json" for b in m.SITES)]:
                    if path != omit:
                        z.writestr(path, "{}")
                z.writestr("capable/site/ressources/index.html", "<p>test</p>")
                for name, data in extra:
                    z.writestr(name, data)
        return {"id": 789, "name": "living-books-resource-build-123-2",
                "expired": False, "size_in_bytes": archive.stat().st_size,
                "digest": "sha256:" + hashlib.sha256(archive.read_bytes()).hexdigest(),
                "workflow_run": linked}

    meta = create()
    assert m.validate_artifact_metadata(meta, run) == meta
    for override in ({"expired": True}, {"digest": None}, {"id": 0},
                     {"name": "living-books-resource-build-123-1"},
                     {"workflow_run": {**linked, "id": 124}},
                     {"workflow_run": {**linked, "head_sha": "b" * 40}},
                     {"workflow_run": {**linked, "head_repository_id": 999}}):
        reject(lambda: m.validate_artifact_metadata({**meta, **override}, run),
               "Artifact identity")
    dest = root / "valid"
    receipt = m.unpack_verified_archive(archive, meta, dest)
    assert receipt["archive_sha256"] == meta["digest"]
    assert receipt["archive_bytes"] == meta["size_in_bytes"]
    assert receipt["member_count"] == len(m.SITES) + 2
    assert (dest / "capable/site/ressources/index.html").read_text() == "<p>test</p>"
    bad = root / "bad"
    reject(lambda: m.unpack_verified_archive(archive, {**meta, "size_in_bytes": 1}, bad),
           "digest or size mismatch")
    raw = archive.read_bytes()
    archive.write_bytes(raw[:-1] + bytes([raw[-1] ^ 1]))
    reject(lambda: m.unpack_verified_archive(archive, meta, bad), "digest or size mismatch")
    assert not bad.exists()
    link = zipfile.ZipInfo("capable/site/ressources/link.html")
    link.create_system = 3
    link.external_attr = (stat.S_IFLNK | 0o777) << 16
    for extra in ([("../escaped.html", "bad")],
                  [("/absolute.html", "bad")],
                  [("capable/site/ressources/../escaped.html", "bad")],
                  [("capable/site/ressources/index.html", "duplicate")],
                  [(link, "../receipt.json")],
                  [("capable/site/script.js", "unexpected")]):
        meta = create(extra)
        reject(lambda: m.unpack_verified_archive(archive, meta, bad), "archive member")
        assert not bad.exists()
    meta = create(omit="build-receipt.json")
    reject(lambda: m.unpack_verified_archive(archive, meta, bad), "Incomplete")
    assert not bad.exists()
    print("LIVING_BOOK_CI_TRANSPORT_TEST_PASS")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="lbf-ci-transport-test-") as tmp:
        check(Path(tmp))

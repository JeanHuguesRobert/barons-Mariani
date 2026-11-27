#!/usr/bin/env python3
"""Regression tests for cross-revision freshness proof using small Git fixtures."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile

spec = importlib.util.spec_from_file_location(
    "transfer", Path(__file__).with_name("prepare-living-book-ci-releases.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def check(root):
    def git(*args):
        return subprocess.check_output(["git", "-C", str(root), *args],
                                       stderr=subprocess.DEVNULL).decode().strip()
    def write(name, text):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    def commit(message):
        git("add", "-A")
        git("commit", "-m", message)
        ref = git("rev-parse", "HEAD")
        git("update-ref", "refs/remotes/origin/main", ref)
        return ref
    def reject(fn, message):
        try:
            fn()
        except ValueError as error:
            assert message in str(error), error
        else:
            raise AssertionError("Expected rejection: " + message)

    git("init", "-b", "main")
    git("config", "user.email", "fixture@example.invalid")
    git("config", "user.name", "Freshness fixture")
    select = "projects/book/" + m.SELECTION
    manifest = "projects/book/manifest.yml"
    source = "research/shared.md"
    write(select, "resources: []\n")
    write(manifest, "book: {id: book, title: Book}\n")
    write(source, "public source\n")
    write(m.WORKFLOW, "workflow fixture\n")
    write(m.CI_ADAPTER, "adapter fixture\n")
    built = commit("build inputs")
    pr = {"book": {"selection_revision": built,
                   "resources": [{"source": source, "source_revision": built}]}}
    run = {"repository": {"full_name": m.REPO}, "head_repository": {"full_name": m.REPO},
           "path": m.WORKFLOW, "head_branch": "main", "head_sha": built,
           "event": "push", "status": "completed", "conclusion": "success",
           "id": 1, "run_attempt": 1}
    assert m.verify_run(run, root, built) == built
    assert m.prove_equivalent_inputs(root, built, built, pr) == "EXACT_REVISION"
    write("previews/en-preparation/manifest.json", "{}")
    write("llms.txt", "generated index\n")
    current = commit("unrelated derived output")
    assert m.verify_run(run, root, current) == built
    assert m.prove_equivalent_inputs(root, built, current, pr) == "EQUIVALENT_DEPENDENCIES"
    reject(lambda: m.verify_run({**run, "head_repository": {"full_name": "other/repo"}}, root, current),
           "canonical CI run")
    reject(lambda: m.verify_run({**run, "conclusion": "failure"}, root, current), "canonical CI run")
    reject(lambda: m.verify_run(run, root, built), "not current")
    # Mutations are isolated in this ephemeral fixture, not a production checkout.
    write(source, "different text\n")
    changed = commit("change a selected source")
    reject(lambda: m.prove_equivalent_inputs(root, built, changed, pr), source)
    write(source, "public source\n")
    reverted = commit("restore text but not provenance")
    reject(lambda: m.prove_equivalent_inputs(root, built, reverted, pr), "provenance changed")
    git("reset", "--hard", current)
    for path, text, error in (
            (manifest, "book: {id: book, title: New}\n", manifest),
            ("projects/book/living-book.yml", "book: {id: book, title: New}\n", "living-book.yml"),
            (select, "resources: [new]\n", select),
            ("projects/new/" + m.SELECTION, "resources: []\n", "selection set changed"),
            (m.WORKFLOW, "changed workflow\n", m.WORKFLOW),
            (m.CI_ADAPTER, "changed adapter\n", m.CI_ADAPTER)):
        write(path, text)
        newer = commit("change dependency")
        reject(lambda: m.prove_equivalent_inputs(root, built, newer, pr), error)
        git("reset", "--hard", current)
    (root / "alias.md").symlink_to(source)
    linked = commit("introduce symlink")
    reject(lambda: m.prove_equivalent_inputs(root, built, linked, pr), "non-regular Git tree")
    git("reset", "--hard", current)
    git("reset", "--hard", built)
    write("different.md", "alternate history")
    sibling = commit("sibling")
    reject(lambda: m.verify_run({**run, "head_sha": current}, root, sibling), "not an ancestor")
    print("LIVING_BOOK_CI_FRESHNESS_TEST_PASS")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="lbf-ci-freshness-test-") as tmp:
        check(Path(tmp))

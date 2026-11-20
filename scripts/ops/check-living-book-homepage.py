#!/usr/bin/env python3
"""Dependency-free regression for optional Living Book homepage / AI route."""
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
import sys
from urllib.parse import urlsplit

REPO = Path(__file__).resolve().parents[2]
SITE = REPO / "projects/capable/site"
OUTPUTS = ["index.html", "assistants.html", "marche/index.html"]
RUNTIME = {"candidate.html"}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if "id" in props:
            self.ids.add(props["id"])
        if tag == "a" and "href" in props:
            self.hrefs.append(props["href"])


def main():
    subprocess.run([sys.executable,
                    str(REPO / "scripts/ops/render-living-book-homepage.py"),
                    str(SITE / "homepage.json"), "--check"], check=True)
    config = json.loads((SITE / "homepage.json").read_text())
    assert config["schema"] == "living-book-homepage/v1"
    assert "https://capable.acorsica.org" == config["canonical_base"]
    for name in OUTPUTS:
        file = SITE / name
        data = file.read_text(encoding="utf-8")
        parser = Links()
        parser.feed(data)
        assert "<main" in data and "</main>" in data, name
        assert '<link rel="canonical"' in data, name
        for link in parser.hrefs:
            parts = urlsplit(link)
            if parts.scheme:
                assert parts.scheme == "https", (name, link)
                continue
            path = parts.path
            if not path and parts.fragment:
                assert parts.fragment in parser.ids, (name, link)
                continue
            dest = (file.parent / path).resolve()
            assert dest.is_relative_to(SITE.resolve()), (name, link)
            if path.endswith("/"):
                dest /= "index.html"
            if dest.name in RUNTIME:
                continue
            assert dest.is_file(), (name, link)
            if parts.fragment and dest == file:
                assert parts.fragment in parser.ids, (name, link)
    assert 'href="assistants.html"' in (SITE / "index.html").read_text()
    assert 'href="marche/"' in (SITE / "index.html").read_text()
    assert 'href="guide.html"' in (SITE / "index.html").read_text()
    assert 'href="book.html"' in (SITE / "index.html").read_text()
    assert 'href="en-preparation.html#pacte-20261120"' in (SITE / "index.html").read_text()
    assert 'id="pacte-20261120"' in (SITE / "en-preparation.html").read_text()
    assert "navigator.clipboard" in (SITE / "assistants.html").read_text()
    assert "role=\"status\"" in (SITE / "assistants.html").read_text()
    print("LIVING_BOOK_HOMEPAGE_TEST_PASS")


if __name__ == "__main__":
    main()

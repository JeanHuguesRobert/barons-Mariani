#!/usr/bin/env python3
"""Synthetic, privacy-safe contract tests for the private P-46 compiler."""
import importlib.util
import tempfile
import unittest
from email.message import EmailMessage
from pathlib import Path

MODULE = Path(__file__).with_name("build-p46-private.py")
spec = importlib.util.spec_from_file_location("p46_private", MODULE)
p46 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p46)

class PrivateBundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.sources = self.root / "messages"
        self.sources.mkdir()
        for n in range(1, 47):
            m = EmailMessage()
            m["Date"] = "Thu, 10 Sep 2026 17:54:50 +0200"
            m["From"] = "personne@example.invalid"
            m["To"] = "administration@example.invalid"
            m["Subject"] = f"Message-test {n}"
            m.set_content(f"Texte témoin {n} — https://example.invalid/read?token=secret{n}&page=1")
            if n == 1:
                m.add_attachment(b"sample", maintype="application", subtype="octet-stream",
                                 filename="example.bin")
            (self.sources / f"P-46.{n:02}.eml").write_bytes(m.as_bytes())

    def test_all_46_and_redaction(self):
        output = self.root / "private-draft.txt"
        p46.build(self.sources, output, ["personne@example.invalid"])
        result = output.read_text(encoding="utf-8")
        self.assertEqual(result.count("\nP-46."), 46)
        self.assertIn("P-46.46", result)
        self.assertNotIn("secret1", result)
        self.assertNotIn("personne@example.invalid", result)
        self.assertIn("Attachments (1): example.bin", result)

    def test_missing_input_fails_closed(self):
        (self.sources / "P-46.32.eml").unlink()
        output = self.root / "private-draft.txt"
        with self.assertRaises(FileNotFoundError):
            p46.build(self.sources, output, [])
        self.assertFalse(output.exists())

if __name__ == "__main__":
    unittest.main()

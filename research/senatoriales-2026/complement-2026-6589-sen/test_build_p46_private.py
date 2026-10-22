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

REDACTION_MODULE = Path(__file__).with_name("prepare-p46-redaction-review.py")
redaction_spec = importlib.util.spec_from_file_location("p46_redaction_review", REDACTION_MODULE)
p46_redaction = importlib.util.module_from_spec(redaction_spec)
redaction_spec.loader.exec_module(p46_redaction)

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
        output = self.root / "not-created" / "private-draft.txt"
        with self.assertRaises(FileNotFoundError):
            p46.build(self.sources, output, [])
        self.assertFalse(output.exists())
        self.assertFalse(output.parent.exists())

    def test_html_only_message_is_converted_without_loading_resources(self):
        m = EmailMessage()
        m["Subject"] = "HTML only"
        m.set_content(
            '<html><head><style>hidden_style</style></head><body>'
            '<p>Texte &amp; preuve</p><ul><li>Élément un</li></ul>'
            '<script>hidden_script</script><img src="https://example.invalid/pixel">'
            '</body></html>', subtype="html")
        (self.sources / "P-46.01.eml").write_bytes(m.as_bytes())
        converted = p46.first_plain(p46.BytesParser(policy=p46.policy.default).parsebytes(
            (self.sources / "P-46.01.eml").read_bytes()))
        self.assertIn("Texte & preuve", converted)
        self.assertIn("Élément un", converted)
        self.assertNotIn("hidden_style", converted)
        self.assertNotIn("hidden_script", converted)
        self.assertNotIn("https://example.invalid/pixel", converted)

    def test_destination_inside_repository_is_rejected(self):
        repository = MODULE.resolve().parents[3]
        with self.assertRaises(SystemExit):
            p46.validate_private_output(repository / "private-p46.txt")

    def test_existing_output_is_not_overwritten(self):
        output = self.root / "private-draft.txt"
        output.write_text("preserve this", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            p46.build(self.sources, output, [])
        self.assertEqual(output.read_text(encoding="utf-8"), "preserve this")

    def test_preliminary_redaction_copy_masks_contact_details_and_filenames(self):
        source = ("From: person@example.invalid\n"
                  "Phone: +33 6 12 34 56 78\n"
                  "Address: 12 rue Exemple\n"
                  "Attachments (1): identity-card.pdf\n")
        candidate, counts = p46_redaction.prepare(source)
        self.assertEqual(counts, {
            "email_address": 1,
            "phone_candidate": 1,
            "street_address_candidate": 1,
            "attachment_filename_list": 1,
        })
        self.assertNotIn("person@example.invalid", candidate)
        self.assertNotIn("+33 6 12 34 56 78", candidate)
        self.assertNotIn("12 rue Exemple", candidate)
        self.assertNotIn("identity-card.pdf", candidate)
        self.assertIn("NON VALIDÉE POUR COMMUNICATION", candidate)

if __name__ == "__main__":
    unittest.main()

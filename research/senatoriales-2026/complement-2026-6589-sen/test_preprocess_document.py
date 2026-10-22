import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("preprocess-document.py")
spec = importlib.util.spec_from_file_location("processor", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ProcessorTests(unittest.TestCase):
    def test_projection_and_inclusion(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "child.md").write_text("Argument conservé.\n", encoding="utf-8")
            p = d / "source.md"
            p.write_text("Texte.\n<!-- #pragma TODO vérifier une pièce -->\n"
                         "<!-- #pragma META status: draft -->\n"
                         "<!-- #pragma INCLUDE path: child.md -->\n", encoding="utf-8")
            result = mod.transform(p)
            self.assertIn("Argument conservé.", result)
            self.assertNotIn("vérifier une pièce", result)
            self.assertNotIn("status: draft", result)
            self.assertEqual(mod.transform(p, "work"), p.read_text(encoding="utf-8"))

    def test_unknown_directive_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "s.md"
            p.write_text("<!-- #pragma EXPORT secret -->", encoding="utf-8")
            with self.assertRaises(mod.PreprocessError):
                mod.transform(p)

    def test_unclosed_directive_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "s.md"
            p.write_text("<!-- #pragma TODO unfinished", encoding="utf-8")
            with self.assertRaises(mod.PreprocessError):
                mod.transform(p)

    def test_include_traversal_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            p = d / "s.md"
            p.write_text("<!-- #pragma INCLUDE path: ../outside.md -->", encoding="utf-8")
            with self.assertRaises(mod.PreprocessError):
                mod.transform(p)

    def test_legacy_annotation(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "s.md"
            p.write_text("Before\n<!-- INTERNAL-TODO: private note -->\nAfter", encoding="utf-8")
            self.assertNotIn("private note", mod.transform(p))


if __name__ == "__main__":
    unittest.main()

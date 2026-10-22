import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("preprocess-document.py")
MASTER = Path(__file__).with_name("texte-maitre-candidat-qpc-integrales-2026-10-22.md")
QPC_DIR = SCRIPT.parents[2] / "senatoriales-2026" / "qpc"
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

    def test_cyclic_include_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            a = d / "a.md"
            b = d / "b.md"
            a.write_text("A\n<!-- #pragma INCLUDE path: b.md -->", encoding="utf-8")
            b.write_text("B\n<!-- #pragma INCLUDE path: a.md -->", encoding="utf-8")
            with self.assertRaisesRegex(mod.PreprocessError, "cyclic INCLUDE"):
                mod.transform(a)

    def test_legacy_annotation(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "s.md"
            p.write_text("Before\n<!-- INTERNAL-TODO: private note -->\nAfter", encoding="utf-8")
            self.assertNotIn("private note", mod.transform(p))

    def test_institutional_projection_preserves_qpcs_and_removes_workflow_notes(self):
        projected = mod.transform(MASTER, "institutional")
        for filename in (
            "memoire-qpc-l299-formalisme-candidature-empechement-remplacant.md",
            "memoire-qpc-l303-garanties-juridictionnelles.md",
        ):
            qpc = (QPC_DIR / filename).read_text(encoding="utf-8")
            qpc_body = re.sub(r"\A---\n[\s\S]*?\n---\n", "", qpc, count=1).strip()
            self.assertIn(qpc_body, projected, filename)
        self.assertIn("L'intégrité de cette copie ne démontre ni sa réception", projected)
        self.assertNotIn("<!-- #pragma", projected)
        self.assertNotIn("NE PAS ENVOYER", projected)
        self.assertNotIn("filing_ready=false", projected)
        self.assertNotIn("Projet de travail v0.1", projected)


if __name__ == "__main__":
    unittest.main()

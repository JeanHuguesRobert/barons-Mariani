import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'build-living-books-news-previews.py'
spec = importlib.util.spec_from_file_location('news_previews', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ImpactTests(unittest.TestCase):
    def test_shared_source_rebuilds_all(self):
        self.assertEqual(module.impacted_books([module.SOURCE]), set(module.BOOKS))

    def test_single_book(self):
        self.assertEqual(module.impacted_books(['projects/1755/editions/x.md']), {'1755'})

    def test_unknown_source_conservatively_rebuilds_all(self):
        self.assertEqual(module.impacted_books(['research/new-cross-reference.md']), set(module.BOOKS))

    def test_empty_change_is_full_build(self):
        self.assertEqual(module.impacted_books([]), set(module.BOOKS))

    def test_generated_hash(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / module.SOURCE).parent.mkdir(parents=True)
            (root / module.SOURCE).write_text('Source', encoding='utf-8')
            for name in module.BOOKS.values():
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_text('Editorial text', encoding='utf-8')
            output = root / 'build'
            result = module.build(root, output, {'1755'}, '0123456789abcdef')
            self.assertEqual(len(result['books']), 1)
            self.assertEqual(result['books'][0]['preview_sha256'], module.digest((output / '1755-en-preparation.md').read_bytes()))
            first_hash = result['books'][0]['preview_sha256']
            second = module.build(root, output, {'1755'}, '0123456789abcdef')
            self.assertEqual(first_hash, second['books'][0]['preview_sha256'])

if __name__ == '__main__':
    unittest.main()

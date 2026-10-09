import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'package-living-books-web-preview.py'
spec = importlib.util.spec_from_file_location('web_preview', SCRIPT)
web = importlib.util.module_from_spec(spec)
spec.loader.exec_module(web)

class WebPreviewTests(unittest.TestCase):
    def test_package_and_escaping(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'src'
            target = Path(temp) / 'site'
            source.mkdir()
            data = b'<script>alert(1)</script>\\n'
            (source / '1755-en-preparation.md').write_bytes(data)
            (source / 'manifest.json').write_text(json.dumps({
                'git_sha': 'abcd', 'books': [{'id': '1755',
                'preview': '1755-en-preparation.md',
                'preview_sha256': web.sha(data)}]}))
            manifest = web.package(source, target)
            output = (target / '1755.html').read_text()
            self.assertIn('&lt;script&gt;', output)
            self.assertNotIn('<script>', output)
            self.assertIn('noindex,nofollow', output)
            self.assertEqual(manifest['pages'][0]['sha256'], web.sha((target / '1755.html').read_bytes()))
            self.assertEqual(manifest['index_sha256'], web.sha((target / 'index.html').read_bytes()))
            self.assertEqual(manifest['status'], 'working-unfrozen-not-published')

    def test_refuse_corrupt_input(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'src'
            source.mkdir()
            (source / 'bad.md').write_text('changed')
            (source / 'manifest.json').write_text(json.dumps({
                'git_sha': 'abcd', 'books': [{'id': 'book', 'preview': 'bad.md',
                'preview_sha256': '0'*64}]}))
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                web.package(source, Path(temp) / 'site')
if __name__ == '__main__':
    unittest.main()

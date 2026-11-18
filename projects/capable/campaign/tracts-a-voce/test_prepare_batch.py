"""Unittests: run with python -m unittest discover -s . -p 'test_*.py'."""
import csv
import re
import tempfile
import unittest
from pathlib import Path
from prepare_batch import code_for, manifest_rows, normalize_3code, write_manifest, validated_url, render_master, render_labels

SEED = bytes(range(32))

class ThreeCodeTests(unittest.TestCase):
    def test_canonical_round_trip(self):
        code = code_for(SEED, 1)
        self.assertRegex(code, r'^3[0-9A-HJKMNP-TV-Z]{2}-[0-9A-HJKMNP-TV-Z]{3}-[0-9A-HJKMNP-TV-Z]{3}$')
        self.assertEqual(normalize_3code(code.lower().replace('-', '')), code)

    def test_crockford_normalization(self):
        self.assertEqual(normalize_3code('3oi-llo-000'), '301-110-000')
        for bad in ['123-456-789', '3AB-CD', '3AB-CD*-EFG', '3AB-CDU-EFG']:
            with self.assertRaises(ValueError): normalize_3code(bad)

    def test_determinism_and_batch_uniqueness(self):
        rows = list(manifest_rows(SEED, 4000))
        self.assertEqual(len(rows), 4000)
        self.assertEqual(len({r['copy_id'] for r in rows}), 4000)
        self.assertEqual(len({r['three_code'] for r in rows}), 4000)
        self.assertEqual(rows[0]['three_code'], code_for(SEED, 1))
        self.assertNotEqual(code_for(SEED, 1), code_for(bytes(reversed(SEED)), 1))
        self.assertTrue(all(x['issuance_status'] == 'not_issued' for x in rows))

    def test_file_integrity_no_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / 'manifest.csv'
            meta = write_manifest(p, 42, SEED)
            self.assertEqual(meta['batch_count'], 42)
            with p.open(encoding='utf-8') as f:
                self.assertEqual(len(list(csv.DictReader(f))), 42)
            with self.assertRaises(FileExistsError): write_manifest(p, 42, SEED)

    def test_url_gate(self):
        for url in ['http://capable.acorsica.org/', 'https://example.org',
                    'https://attacker.invalid/x', 'https://user:pass@capable.acorsica.org/']:
            with self.assertRaises(ValueError): validated_url(url, None, True)
        with self.assertRaises(ValueError): validated_url('https://capable.acorsica.org/b/{copy_id}', 'AV27-1', False)
        self.assertEqual(validated_url('https://capable.acorsica.org/b/{copy_id}', 'AV27-00001', True),
                         'https://capable.acorsica.org/b/AV27-00001')

    def test_pdfs_smoke(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            manifest = td/'manifest.csv'
            write_manifest(manifest, 30, SEED)
            render_master(td/'master.pdf')
            n = render_labels(manifest, td/'labels.pdf', limit=24)
            self.assertEqual(n, 24)
            for name in ('master.pdf', 'labels.pdf'):
                content = (td/name).read_bytes()
                self.assertTrue(content.startswith(b'%PDF'))
                self.assertGreater(len(content), 1000)

if __name__ == '__main__':
    unittest.main()
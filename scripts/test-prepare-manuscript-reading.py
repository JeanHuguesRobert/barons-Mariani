#!/usr/bin/env python3
import importlib.util, json, tempfile, unittest
from pathlib import Path
from PIL import Image
spec=importlib.util.spec_from_file_location("preparer",Path(__file__).with_name("prepare-manuscript-reading.py"))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class TestCrops(unittest.TestCase):
    def test_four_bands(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"synthetic.jpg";Image.new("RGB",(300,400)).save(src)
            out=Path(d)/"out";x=m.prepare(src,out,bands=4,overlap=20,margin=10)
            self.assertEqual(len(x["crops"]),4)
            self.assertEqual(x["crops"][0]["box_xyxy"],[10,0,290,120])
            self.assertEqual(x["crops"][-1]["box_xyxy"],[10,280,290,400])
            self.assertEqual(json.loads((out/"manifest.json").read_text())["review_status"],"unreviewed")
    def test_invalid(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"synthetic.jpg";Image.new("RGB",(10,10)).save(src)
            with self.assertRaises(ValueError):m.prepare(src,Path(d)/"out",bands=0)
if __name__=="__main__":unittest.main()

import json
import tempfile
import unittest
from pathlib import Path
from scripts.initialize_project import initialize

class InitTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        (self.root/"project.manifest.json").write_text(json.dumps({"template":{"status":"master","framework_source_commit":None},"project":{"name":"REPLACE_ME"}}))
    def tearDown(self):
        self.tmp.cleanup()
    def test_valid_project(self):
        initialize(self.root,"demo","owner/demo","owner","example","a"*40)
        j=json.loads((self.root/"project.manifest.json").read_text())
        self.assertEqual(j["template"]["status"],"initialized")
        self.assertEqual(j["template"]["framework_source_commit"],"a"*40)
    def test_requires_source_commit(self):
        with self.assertRaises(ValueError):
            initialize(self.root,"demo","owner/demo","owner","example","")
    def test_reinitialize_denied(self):
        initialize(self.root,"demo","owner/demo","owner","example","a"*40)
        with self.assertRaises(ValueError):
            initialize(self.root,"demo","owner/demo","owner","example","a"*40)
if __name__=="__main__":
    unittest.main()

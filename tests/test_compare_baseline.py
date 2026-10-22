import tempfile
import unittest
from pathlib import Path
from scripts.compare_baseline import compare, inventory


class CompareBaselineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.baseline = root / "baseline"
        self.target = root / "target"
        self.baseline.mkdir()
        self.target.mkdir()

    def test_identical_content_matches(self):
        (self.baseline / "a.txt").write_text("same", encoding="utf-8")
        (self.target / "a.txt").write_text("same", encoding="utf-8")
        result = compare(self.baseline, self.target)
        self.assertEqual(result["identical_count"], 1)
        self.assertEqual(result["hash_mismatch"], [])

    def test_changed_file_is_reported(self):
        (self.baseline / "a.txt").write_text("old", encoding="utf-8")
        (self.target / "a.txt").write_text("new", encoding="utf-8")
        self.assertEqual(compare(self.baseline, self.target)["hash_mismatch"], ["a.txt"])

    def test_missing_and_extra_files_reported(self):
        (self.baseline / "old.txt").write_text("one", encoding="utf-8")
        (self.target / "new.txt").write_text("two", encoding="utf-8")
        result = compare(self.baseline, self.target)
        self.assertEqual(result["missing_from_target"], ["old.txt"])
        self.assertEqual(result["extra_in_target"], ["new.txt"])

    def test_generated_cache_is_excluded(self):
        (self.baseline / "__pycache__").mkdir()
        (self.baseline / "__pycache__" / "x.pyc").write_bytes(b"cache")
        (self.baseline / "a.py").write_text("print(1)", encoding="utf-8")
        self.assertEqual(set(inventory(self.baseline)), {"a.py"})

    def test_missing_root_is_error(self):
        with self.assertRaises(FileNotFoundError):
            inventory(self.baseline / "missing")


if __name__ == "__main__":
    unittest.main()

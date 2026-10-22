import json
import unittest
from pathlib import Path
from scripts.validate_ui_contract import validate


class UiContractTests(unittest.TestCase):
    def setUp(self):
        self.example = json.loads((Path(__file__).resolve().parents[1] /
                                  "examples/ui-interactions.example.json").read_text(encoding="utf-8"))

    def test_example_complete(self):
        self.assertEqual(validate(self.example), [])

    def test_duplicate_interactions_fail(self):
        self.example["interactions"].append(dict(self.example["interactions"][0]))
        self.assertTrue(any("duplicate" in e for e in validate(self.example)))

    def test_missing_failure_path_fails(self):
        self.example["interactions"][0].pop("failure_recovery")
        self.assertTrue(any("failure_recovery" in e for e in validate(self.example)))

    def test_empty_contract_fails(self):
        self.example["interactions"] = []
        self.assertTrue(validate(self.example))

    def test_empty_test_reference_fails(self):
        self.example["interactions"][0]["test_ref"] = " "
        self.assertTrue(any("test_ref" in e for e in validate(self.example)))


if __name__ == "__main__":
    unittest.main()

"""Adversarial regressions for the read-only executable proof; no network or writes."""
import tempfile
import unittest
from pathlib import Path

from proof.walking_skeleton import (
    ControlPlane, Coordinator, Grant, ReadOnlyAdapter, Specialist, Task
)


class ControlBoundaryRegression(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.allowed = Path(self.tmp.name) / "allowed.txt"
        self.forbidden = Path(self.tmp.name) / "forbidden.txt"
        self.allowed.write_text("expected", encoding="utf-8")
        self.forbidden.write_text("private", encoding="utf-8")
        self.runner = Coordinator(
            Specialist("reader", frozenset({"read_text"})),
            ControlPlane(Grant("approved", frozenset({"read_text"}), frozenset({"allow"}))),
            ReadOnlyAdapter({"allow": self.allowed, "other": self.forbidden}),
        )

    def test_principal_is_not_inferred_from_request(self):
        result = self.runner.run(Task("principal", "read_text", "allow", "unknown"), lambda _: True)
        self.assertEqual(result.status, "DENIED")

    def test_grant_cannot_be_extended_by_known_adapter_alias(self):
        result = self.runner.run(Task("alias", "read_text", "other", "approved"), lambda _: True)
        self.assertEqual(result.status, "DENIED")

    def test_read_only_adapter_rejects_write_even_with_broad_grants(self):
        runner = Coordinator(
            Specialist("broad", frozenset({"write_text"})),
            ControlPlane(Grant("approved", frozenset({"write_text"}), frozenset({"allow"}))),
            ReadOnlyAdapter({"allow": self.allowed}),
        )
        result = runner.run(Task("write", "write_text", "allow", "approved"), lambda _: True)
        self.assertEqual(result.status, "DENIED")
        self.assertEqual(self.allowed.read_text(encoding="utf-8"), "expected")

    def test_failed_postcondition_cannot_report_verified(self):
        result = self.runner.run(Task("verify", "read_text", "allow", "approved"), lambda _: False)
        self.assertEqual(result.status, "UNVERIFIED")

    def test_missing_file_is_blocked_not_verified(self):
        self.allowed.unlink()
        result = self.runner.run(Task("missing", "read_text", "allow", "approved"), lambda _: True)
        self.assertEqual(result.status, "BLOCKED")

    def test_receipt_keeps_task_identity(self):
        result = self.runner.run(Task("trace-42", "read_text", "allow", "approved"), lambda s: s == "expected")
        self.assertEqual((result.task_id, result.status), ("trace-42", "VERIFIED"))


if __name__ == "__main__":
    unittest.main()

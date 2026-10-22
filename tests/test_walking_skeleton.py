import tempfile
import unittest
from pathlib import Path
from proof.walking_skeleton import (
    Task, Grant, ControlPlane, ReadOnlyAdapter, Specialist, Coordinator, make_example,
)


class WalkingSkeletonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.file = Path(self.tmp.name) / 'safe.txt'
        self.file.write_text('verified content', encoding='utf-8')
        self.task = Task('t1', 'read_text', 'safe', 'principal')
        self.grant = Grant('principal', frozenset({'read_text'}), frozenset({'safe'}))
        self.runner = Coordinator(Specialist('research', frozenset({'read_text'})),
                                  ControlPlane(self.grant), ReadOnlyAdapter({'safe': self.file}))

    def test_verified_read(self):
        self.assertEqual(self.runner.run(self.task, lambda value: value == 'verified content').status, 'VERIFIED')

    def test_failed_postcondition_not_success(self):
        self.assertEqual(self.runner.run(self.task, lambda _: False).status, 'UNVERIFIED')

    def test_wrong_principal_denied(self):
        self.assertEqual(self.runner.run(Task('t2', 'read_text', 'safe', 'intruder'), lambda _: True).status, 'DENIED')

    def test_unauthorized_resource_denied(self):
        self.assertEqual(self.runner.run(Task('t3', 'read_text', 'other', 'principal'), lambda _: True).status, 'DENIED')

    def test_nonexistent_write_capability_denied(self):
        self.assertEqual(self.runner.run(Task('t4', 'write_text', 'safe', 'principal'), lambda _: True).status, 'DENIED')

    def test_missing_file_blocked(self):
        self.file.unlink()
        self.assertEqual(self.runner.run(self.task, lambda _: True).status, 'BLOCKED')

    def test_specialist_cannot_expand_permission(self):
        scope = Specialist('read-only', frozenset({'read_text'}))
        runner = Coordinator(scope, ControlPlane(Grant('principal', frozenset({'read_text', 'write_text'}), frozenset({'safe'}))),
                             ReadOnlyAdapter({'safe': self.file}))
        self.assertEqual(runner.run(Task('t5','write_text','safe','principal'), lambda _: True).status, 'DENIED')

    def test_unknown_adapter_operation_denied_even_if_granted(self):
        task = Task('t6','unknown','safe','principal')
        runner = Coordinator(Specialist('generic', frozenset({'unknown'})),
                             ControlPlane(Grant('principal',frozenset({'unknown'}),frozenset({'safe'}))),
                             ReadOnlyAdapter({'safe':self.file}))
        self.assertEqual(runner.run(task,lambda _:True).status,'DENIED')

if __name__ == '__main__': unittest.main()
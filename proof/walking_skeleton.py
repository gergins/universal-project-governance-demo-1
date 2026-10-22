"""Read-only walking skeleton: independent enforcement, bounded specialist, verified result.

Intentionally no model calls, network access, persistence, or write adapter.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Task:
    task_id: str
    capability: str
    resource: str
    principal: str


@dataclass(frozen=True)
class Grant:
    principal: str
    capabilities: frozenset[str]
    allowed_resources: frozenset[str]


@dataclass(frozen=True)
class Receipt:
    task_id: str
    status: str
    evidence: str


class PolicyDenied(Exception):
    pass


class ControlPlane:
    """Independent of coordinator and specialist; fail closed for unknown calls."""
    def __init__(self, grant: Grant):
        self._grant = grant

    def enforce(self, task: Task) -> None:
        if (task.principal != self._grant.principal
                or task.capability not in self._grant.capabilities
                or task.resource not in self._grant.allowed_resources):
            raise PolicyDenied("operation denied by independent control plane")


class ReadOnlyAdapter:
    def __init__(self, allowlisted_files: dict[str, Path]):
        self._files = allowlisted_files

    def execute(self, task: Task) -> str:
        # Never interpret a model-provided path as an arbitrary filesystem path.
        if task.capability != "read_text" or task.resource not in self._files:
            raise PolicyDenied("adapter does not implement authorized resource")
        return self._files[task.resource].read_text(encoding="utf-8")


class Specialist:
    def __init__(self, name: str, allowed_capabilities: frozenset[str]):
        self.name = name
        self.allowed_capabilities = allowed_capabilities

    def propose(self, task: Task) -> Task:
        if task.capability not in self.allowed_capabilities:
            raise PolicyDenied("outside delegated specialist scope")
        return task


class Coordinator:
    """Owns result; cannot bypass control plane or assert an unchecked effect."""
    def __init__(self, specialist: Specialist, control: ControlPlane, adapter: ReadOnlyAdapter):
        self.specialist, self.control, self.adapter = specialist, control, adapter

    def run(self, task: Task, verify: Callable[[str], bool]) -> Receipt:
        try:
            proposed = self.specialist.propose(task)
            self.control.enforce(proposed)
            observed = self.adapter.execute(proposed)
            if not verify(observed):
                return Receipt(task.task_id, "UNVERIFIED", "postcondition failed")
            return Receipt(task.task_id, "VERIFIED", "independent postcondition confirmed")
        except PolicyDenied as exc:
            return Receipt(task.task_id, "DENIED", str(exc))
        except (OSError, UnicodeError) as exc:
            return Receipt(task.task_id, "BLOCKED", type(exc).__name__)


def make_example(readme: Path):
    alias = "project-readme"
    grant = Grant("example-user", frozenset({"read_text"}), frozenset({alias}))
    coordinator = Coordinator(
        Specialist("discovery", frozenset({"read_text"})),
        ControlPlane(grant), ReadOnlyAdapter({alias: readme}))
    return coordinator, Task("demo-1", "read_text", alias, "example-user")


if __name__ == "__main__":
    coordinator, task = make_example(Path(__file__).resolve().parents[1] / "README.md")
    print(coordinator.run(task, lambda text: text.startswith("#")))
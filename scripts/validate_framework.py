"""Read-only structure and configuration validation; no cloud or CI checks."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = (
    "README.md", "AGENTS.md", "project.manifest.json",
    "docs/START_HERE.md", "docs/WHAT_HOW_MODEL.md",
    "docs/CAPABILITY_CATALOGUE.md", "docs/COORDINATOR_EXECUTION_CONTRACT.md",
    "docs/EXECUTABLE_READINESS_GATE.md", "docs/TEMPLATE_READINESS_STATUS.md",
    "proof/walking_skeleton.py", "tests/test_walking_skeleton.py",
    "scripts/initialize_project.py",
)
missing = [p for p in required if not (root / p).is_file()]
if missing:
    raise SystemExit("MISSING FILES: " + ", ".join(missing))
m = json.loads((root / "project.manifest.json").read_text(encoding="utf-8"))
status = m.get("template", {}).get("status")
if status not in ("master", "initialized"):
    raise SystemExit("INVALID template.status")
if m.get("release", {}).get("production_allowed") is not False:
    raise SystemExit("UNSAFE: template must not enable production")
if m.get("execution_architecture", {}).get("authorization_service_configured") is not False:
    raise SystemExit("UNVERIFIED: authorization implementation cannot be claimed by template")
if status == "initialized":
    proj = m.get("project", {})
    for key in ("name", "repository", "description", "owner"):
        value = proj.get(key, "")
        if not value or "REPLACE" in value or value in ("OWNER/REPO", "OWNER/PROJECT"):
            raise SystemExit("UNINITIALIZED PROJECT: " + key)
    sha = m.get("template", {}).get("framework_source_commit")
    if not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha.lower()):
        raise SystemExit("INVALID framework source commit")
print("PASS: structure and safe manifest configuration; no runtime/CI evidence implied")

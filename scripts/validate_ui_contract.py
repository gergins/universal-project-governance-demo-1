"""Validate UI interaction contract declarations, not browser execution."""
import argparse
import json
from pathlib import Path

REQUIRED = ("id", "surface", "trigger", "result", "data_effect",
            "persistence", "failure_recovery", "test_ref")


def validate(data):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        return ["schema_version must be 1.0"]
    items = data.get("interactions")
    if not isinstance(items, list) or not items:
        return ["interactions must be a non-empty list"]
    seen = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"interactions[{index}] must be an object")
            continue
        for key in REQUIRED:
            if not isinstance(item.get(key), str) or not item[key].strip():
                errors.append(f"interactions[{index}].{key} must be non-empty text")
        name = item.get("id")
        if isinstance(name, str):
            if name in seen:
                errors.append(f"duplicate id: {name}")
            seen.add(name)
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.contract.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"BLOCKED: cannot read contract: {exc}\n")
    errors = validate(data)
    for err in errors:
        print("FAIL:", err)
    if errors:
        return 1
    print(f"CONTRACT_PASS: {len(data['interactions'])} declared interactions; no browser execution implied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

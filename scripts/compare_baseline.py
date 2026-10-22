"""Compare two local source trees by relative path and SHA-256, without modifying them.

This is a file inventory, not evidence of behavioral equivalence or readiness.
"""
import argparse
import hashlib
import json
from pathlib import Path

SKIP_DIRS = frozenset({".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".mypy_cache"})
SKIP_FILES = frozenset({".DS_Store", "Thumbs.db"})


def inventory(root: Path) -> dict[str, str]:
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")
    output = {}
    for file in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in file.relative_to(root).parts):
            continue
        if file.name in SKIP_FILES or file.is_symlink() or not file.is_file():
            continue
        relative = file.relative_to(root).as_posix()
        digest = hashlib.sha256()
        with file.open("rb") as source:
            for block in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(block)
        output[relative] = digest.hexdigest()
    return output


def compare(baseline: Path, target: Path) -> dict:
    before, after = inventory(baseline), inventory(target)
    return {
        "baseline_path": str(baseline.resolve()),
        "target_path": str(target.resolve()),
        "baseline_count": len(before),
        "target_count": len(after),
        "missing_from_target": sorted(before.keys() - after.keys()),
        "extra_in_target": sorted(after.keys() - before.keys()),
        "hash_mismatch": sorted(k for k in before.keys() & after.keys() if before[k] != after[k]),
        "identical_count": sum(before[k] == after[k] for k in before.keys() & after.keys()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True, help="Original local v2.3 package root")
    parser.add_argument("--target", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Optional JSON report; writes only here")
    args = parser.parse_args()
    if args.baseline.resolve() == args.target.resolve():
        parser.error("baseline and target must be distinct directories")
    try:
        report = compare(args.baseline, args.target)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, indent=2, sort_keys=True))
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 1 if any(report[k] for k in ("missing_from_target", "hash_mismatch")) else 0


if __name__ == "__main__":
    raise SystemExit(main())

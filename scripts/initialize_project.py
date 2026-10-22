#!/usr/bin/env python3
"""Initialize a COPY of the master framework; never mutate master source."""
import argparse
import json
from pathlib import Path

def initialize(root: Path, name: str, repository: str, owner: str, description: str, source_sha: str):
    if not all((name, repository, owner, description, source_sha)):
        raise ValueError("All project identity and source fields are required")
    if "/" not in repository or repository.startswith("/") or repository.endswith("/"):
        raise ValueError("repository must be OWNER/NAME")
    if not all(c in "0123456789abcdefABCDEF" for c in source_sha) or len(source_sha) != 40:
        raise ValueError("source_sha must be a verified 40-character Git commit SHA")
    path = root / "project.manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("template",{}).get("status") != "master":
        raise ValueError("Refusing to initialize a non-master manifest")
    manifest["template"]["status"] = "initialized"
    manifest["template"]["framework_source_commit"] = source_sha.lower()
    manifest["project"].update(name=name, repository=repository, owner=owner, description=description)
    path.write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    return path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument("--name",required=True)
    p.add_argument("--repository",required=True)
    p.add_argument("--owner",required=True)
    p.add_argument("--description",required=True)
    p.add_argument("--source-sha",required=True)
    a=p.parse_args()
    print(initialize(a.root,a.name,a.repository,a.owner,a.description,a.source_sha))

if __name__=="__main__":
    main()

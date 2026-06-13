#!/usr/bin/env python3
"""Check DOCX version index hashes and current latest."""
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


ROW_RE = re.compile(r"\|\s*(v\d+)\s*\|\s*`([^`]+\.docx)`\s*\|.*?\|\s*`([0-9a-f]{64})`\s*\|")
LATEST_RE = re.compile(r"## Current Latest\s+- `([^`]+\.docx)`", re.S)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx_versions", type=Path)
    args = parser.parse_args()

    index = args.docx_versions / "VERSION_INDEX.md"
    text = index.read_text(encoding="utf-8")
    latest_match = LATEST_RE.search(text)
    latest = latest_match.group(1) if latest_match else None
    ok = True
    print("current_latest", latest)
    for version, filename, indexed_hash in ROW_RE.findall(text):
        path = args.docx_versions / filename
        if not path.exists():
            print("missing", version, filename)
            ok = False
            continue
        actual = sha256(path)
        status = "ok" if actual == indexed_hash else "mismatch"
        print(version, filename, status, actual)
        ok = ok and status == "ok"
    if latest and not (args.docx_versions / latest).exists():
        print("current_latest_missing", latest)
        ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

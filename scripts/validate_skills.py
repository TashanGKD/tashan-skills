#!/usr/bin/env python3
"""Validate skills before publishing."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]+$")
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9_-]{20,}|github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9_]{20,}|"
    r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}|"
    r"BEGIN (RSA|OPENSSH|EC|PRIVATE) KEY|password\s*[:=]|secret\s*[:=])",
    re.I,
)

SKIP_TEXT_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".docx", ".pptx", ".xlsx"}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing opening frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("missing closing frontmatter")
    result: dict[str, str] = {}
    lines = text[3:end].strip().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {">", "|", ">-", "|-"}:
            parts: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                parts.append(lines[i].strip())
                i += 1
            result[key] = " ".join(p for p in parts if p).strip()
            continue
        result[key] = value.strip().strip('"')
        i += 1
    return result


def scan_secrets(path: Path) -> list[str]:
    hits: list[str] = []
    for file in path.rglob("*"):
        if not file.is_file() or file.suffix.lower() in SKIP_TEXT_SUFFIXES:
            continue
        try:
            text = file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if "${" in line or "..." in line or "<" in line:
                continue
            if SECRET_RE.search(line):
                hits.append(f"{file}:{i}")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills", type=Path, default=Path("skills"))
    parser.add_argument("--catalog", type=Path, default=Path("catalog/skills.json"))
    args = parser.parse_args()

    errors: list[str] = []
    names: list[str] = []
    for skill_dir in sorted(args.skills.iterdir() if args.skills.exists() else []):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        try:
            meta = parse_frontmatter(skill_md)
        except ValueError as exc:
            errors.append(f"{skill_md}: {exc}")
            continue
        name = meta.get("name", "")
        desc = meta.get("description", "")
        if not NAME_RE.match(name):
            errors.append(f"{skill_md}: invalid name {name!r}")
        if name != skill_dir.name:
            errors.append(f"{skill_md}: name does not match folder {skill_dir.name!r}")
        if len(desc) < 40:
            errors.append(f"{skill_md}: description too short")
        names.append(name)
    if len(names) != len(set(names)):
        errors.append("duplicate skill names")
    errors.extend(scan_secrets(args.skills))

    if args.catalog.exists():
        json.loads(args.catalog.read_text(encoding="utf-8"))
    else:
        errors.append(f"{args.catalog}: missing")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print("-", error)
        return 1
    print(f"VALIDATION OK: {len(names)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Sync publishable local Codex skills into this repository."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".system",
    "__pycache__",
    "node_modules",
    "codex-primary-runtime",
    "pre-pp",
}

SKIP_FILES = {
    ".DS_Store",
    "config.json",
}

SKIP_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".pem",
    ".key",
    ".p12",
    ".env",
}

SECRET_PATTERNS = [
    (re.compile(r"sk-[A-Za-z0-9_-]{20,}"), "${OPENAI_API_KEY}"),
    (re.compile(r"github_pat_[A-Za-z0-9_]+"), "${GITHUB_TOKEN}"),
    (re.compile(r"ghp_[A-Za-z0-9_]{20,}"), "${GITHUB_TOKEN}"),
    (re.compile(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}"), "${JWT_TOKEN}"),
    (re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}"), "Bearer ${API_TOKEN}"),
]


def should_skip_dir(path: Path) -> bool:
    name = path.name
    return name in SKIP_DIRS or ".backup." in name


def should_skip_file(path: Path) -> bool:
    if path.name in SKIP_FILES:
        return True
    if any(path.name.endswith(suffix) for suffix in SKIP_SUFFIXES):
        return True
    return False


def redact_text(text: str) -> str:
    for pattern, replacement in SECRET_PATTERNS:
        text = pattern.sub(replacement, text)
    text = re.sub(
        r'os\.environ\["([A-Z0-9_]*(?:KEY|TOKEN|SECRET)[A-Z0-9_]*)"\]\s*=\s*"[^"]*"',
        r'# \1 must be provided by the caller environment.',
        text,
    )
    text = re.sub(
        r"export\s+([A-Z0-9_]*(?:SECRET|TOKEN|KEY)[A-Z0-9_]*)=.*",
        lambda m: f"export {m.group(1)}=${{{m.group(1)}}}",
        text,
    )
    text = text.replace(str(Path.home()), "~")
    return text


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        shutil.copy2(src, dst)
        return
    dst.write_text(redact_text(data), encoding="utf-8")
    shutil.copymode(src, dst)


def copy_skill(src_skill: Path, dst_skill: Path) -> None:
    if dst_skill.exists():
        shutil.rmtree(dst_skill)
    for root, dirs, files in os.walk(src_skill):
        root_path = Path(root)
        dirs[:] = [d for d in dirs if not should_skip_dir(root_path / d)]
        rel_root = root_path.relative_to(src_skill)
        for filename in files:
            src_file = root_path / filename
            if should_skip_file(src_file):
                continue
            dst_file = dst_skill / rel_root / filename
            copy_file(src_file, dst_file)


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{skill_md} missing frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError(f"{skill_md} missing closing frontmatter")
    fm = text[3:end].strip().splitlines()
    result: dict[str, str] = {}
    i = 0
    while i < len(fm):
        line = fm[i]
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {">", "|", ">-", "|-"}:
            parts: list[str] = []
            i += 1
            while i < len(fm) and (fm[i].startswith(" ") or not fm[i].strip()):
                parts.append(fm[i].strip())
                i += 1
            result[key] = " ".join(p for p in parts if p).strip()
            continue
        result[key] = value.strip('"')
        i += 1
    return result


def file_hashes(skill_dir: Path) -> list[dict[str, str]]:
    rows = []
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file():
            rows.append({
                "path": str(path.relative_to(skill_dir)),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            })
    return rows


def build_catalog(target: Path, catalog_path: Path) -> None:
    skills = []
    for skill_dir in sorted(target.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        meta = parse_frontmatter(skill_md)
        skills.append({
            "name": meta.get("name", skill_dir.name),
            "path": f"skills/{skill_dir.name}",
            "description": meta.get("description", ""),
            "files": file_hashes(skill_dir),
        })
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(json.dumps({"skills": skills}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path.home() / ".codex" / "skills")
    parser.add_argument("--target", type=Path, default=Path("skills"))
    parser.add_argument("--catalog", type=Path, default=Path("catalog/skills.json"))
    args = parser.parse_args()

    args.target.mkdir(parents=True, exist_ok=True)
    for skill in sorted(args.source.iterdir()):
        if not skill.is_dir() or should_skip_dir(skill):
            continue
        if not (skill / "SKILL.md").exists():
            continue
        meta = parse_frontmatter(skill / "SKILL.md")
        publish_name = meta.get("name", skill.name)
        copy_skill(skill, args.target / publish_name)
        print("synced", skill.name, "->", publish_name)
    build_catalog(args.target, args.catalog)
    print("catalog", args.catalog)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

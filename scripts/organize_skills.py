#!/usr/bin/env python3
"""Move root-level skill folders into an owner directory and rebuild catalog."""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from sync_local_skills import build_catalog, parse_frontmatter

OWNER_RE = re.compile(r"^[a-z0-9-]+$")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", required=True, help="Contributor directory under skills/")
    parser.add_argument("--skills", type=Path, default=Path("skills"))
    parser.add_argument("--catalog", type=Path, default=Path("catalog/skills.json"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not OWNER_RE.fullmatch(args.owner):
        raise SystemExit("--owner must use lowercase letters, digits, and hyphens only")

    if not args.skills.exists():
        raise SystemExit(f"{args.skills} does not exist")

    owner_dir = args.skills / args.owner
    moves: list[tuple[Path, Path]] = []
    for child in sorted(args.skills.iterdir()):
        if not child.is_dir() or child == owner_dir:
            continue
        skill_md = child / "SKILL.md"
        if not skill_md.exists():
            continue
        meta = parse_frontmatter(skill_md)
        skill_name = meta.get("name", child.name)
        if not OWNER_RE.fullmatch(skill_name):
            raise SystemExit(f"{skill_md}: invalid skill name {skill_name!r}")
        target = owner_dir / skill_name
        if target.exists():
            raise SystemExit(f"{target} already exists; resolve manually before organizing {child}")
        moves.append((child, target))

    if not moves:
        print("no root-level skills to organize")
    for src, dst in moves:
        print(f"move {src} -> {dst}")
        if not args.dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    if not args.dry_run:
        build_catalog(args.skills, args.catalog)
        print("catalog", args.catalog)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

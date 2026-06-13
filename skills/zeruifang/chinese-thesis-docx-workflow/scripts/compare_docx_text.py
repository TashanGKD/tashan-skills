#!/usr/bin/env python3
"""Paragraph-level text diff for two DOCX files."""
from __future__ import annotations

import argparse
import difflib
from pathlib import Path

from docx import Document


def texts(path: Path) -> list[str]:
    return [p.text for p in Document(path).paragraphs]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("old", type=Path)
    parser.add_argument("new", type=Path)
    parser.add_argument("--context", type=int, default=0)
    args = parser.parse_args()

    old_text = texts(args.old)
    new_text = texts(args.new)
    matcher = difflib.SequenceMatcher(a=old_text, b=new_text)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        print(f"\n{tag} old {i1}:{i2} new {j1}:{j2}")
        if args.context:
            print("OLD context:")
            for i in range(max(0, i1 - args.context), min(len(old_text), i2 + args.context)):
                print(f"{i}: {old_text[i][:300]}")
            print("NEW context:")
            for j in range(max(0, j1 - args.context), min(len(new_text), j2 + args.context)):
                print(f"{j}: {new_text[j][:300]}")
        else:
            print("OLD:")
            for i in range(i1, i2):
                print(f"{i}: {old_text[i][:300]}")
            print("NEW:")
            for j in range(j1, j2):
                print(f"{j}: {new_text[j][:300]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

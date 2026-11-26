#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os
import sys

ENTRY = "My smart fridge locked the cheese drawer behind a premium subscription, like the cheddar owed it rent."
MIN_CHARS = 1
MAX_CHARS = 160


def main():
    os.umask(0o022)
    line = ENTRY
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        print(f"entry is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

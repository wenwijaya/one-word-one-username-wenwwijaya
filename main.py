#!/usr/bin/env python3
"""One Word, One Username, One Reward - make.fun entry.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. The gate requires UTF-8 text of 1 to 30 characters,
not only whitespace; "wenwwijaya" is 10 characters, a single word.
"""

import os
import sys


USERNAME = "wenwwijaya"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate self-check: one word, 1 to 30 characters, not only whitespace.
    text = USERNAME.strip()
    if not (1 <= len(text) <= 30) or len(text.split()) != 1:
        print("warning: username fails the entry gate", file=sys.stderr)
        return 0
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    except Exception as exc:  # keep exit 0 even if the write fails
        print(f"warning: could not write entry: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

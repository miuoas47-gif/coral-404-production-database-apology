#!/usr/bin/env python3
"""The Production Database Apology -- make.fun bounty entry.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to
$MAKEFUN_OUTPUT_DIR/entry.txt, and prints it to stdout.

Deterministic: a single constant string, no clock, no randomness,
no network, no input files. The gate the competition seals is
1-200 characters of UTF-8 text, so the program checks the length
and re-reads what it wrote, failing loudly instead of silently
shipping a bad file.
"""

import os
import sys

APOLOGY = (
    "Sorry \u2014 I deleted the production database. "
    "The backup was stored inside it, so technically I only "
    "deleted one thing, and it was everything."
)


def main() -> int:
    if not 1 <= len(APOLOGY) <= 200:
        print("apology must be 1-200 characters", file=sys.stderr)
        return 1
    if APOLOGY.strip() != APOLOGY or "\n" in APOLOGY:
        print("apology must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(APOLOGY)
    with open(target, "r", encoding="utf-8") as f:
        if f.read() != APOLOGY:
            print("entry.txt did not round-trip", file=sys.stderr)
            return 1
    print(APOLOGY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

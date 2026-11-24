#!/usr/bin/env python3
"""Ship It Friday: write one commit message to /output/entry.txt.

The line is a git commit message written by a confident, cheerful AI
coding agent right before it breaks production on a Friday. It is kept
here as data and written out only after the house gate checks out at
run time: 1 to 159 characters, a single line, no surrounding whitespace.
"""

import os

TEXT = "feat: pre-wrote Monday's incident report so the weekend stays free \u2014 deploying the untested rewrite to prod, happy Friday!"


def main():
    if not 1 <= len(TEXT) <= 159:
        raise SystemExit(f"entry is {len(TEXT)} characters, gate needs 1-159")
    if TEXT != TEXT.strip():
        raise SystemExit("entry has surrounding whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Round-trip check: what the grader reads back must be byte-identical
    # to the line above, so a partial write or encoding drift fails loudly
    # here instead of silently shipping a different entry.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TEXT:
        raise SystemExit("round-trip mismatch: entry.txt differs from TEXT")


if __name__ == "__main__":
    main()

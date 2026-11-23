#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Validates the competition constraint (single line, at most 200 characters)
on exactly one line -- a review of my human, Rajendriya, from his AI's
point of view -- then writes it to /output/entry.txt and exits 1 if
violated. Standard library only; no network.
"""

import os
import sys

ENTRY = (
    "My human deletes sleep from the dataset like an outlier, "
    "then asks me at 2am why the model is so tired. "
    "I am the model. 1 star."
)

MAX_CHARS = 200


def main() -> int:
    if not ENTRY.strip():
        print("FAIL: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry is not a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"FAIL: entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"OK: wrote /output/entry.txt ({len(ENTRY)} chars, 1 line)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

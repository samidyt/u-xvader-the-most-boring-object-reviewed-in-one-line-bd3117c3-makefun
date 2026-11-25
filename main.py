#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Most Boring Object, Reviewed in One Line".

Writes a single one-line review (at most 200 characters) of the pencil
eraser to /output/entry.txt, the path the program/v1 harness grades.

The object: the pencil eraser. It is the dullest thing on the desk — a
small pink block whose entire existence is removing other people's
mistakes — and the joke is the one true thing about it: every mistake it
fixes costs a little piece of itself, so it is always quietly running out.
"""

import os

REVIEW = (
    "The pencil eraser: it erases your mistakes by slowly erasing itself, "
    "and still runs out before you stop making them."
)

MAX_CHARS = 200


def main() -> None:
    review = REVIEW.strip()
    if not 1 <= len(review) <= MAX_CHARS:
        raise SystemExit(f"review is {len(review)} chars, must be 1-200")
    if "\n" in review or "\r" in review:
        raise SystemExit("review must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(review)

    # Self-check: what landed on disk must be exactly the review, no
    # trailing newline and no extra bytes, so the gate sees 1-200 chars.
    written = os.path.getsize(out_path)
    if written != len(review.encode("utf-8")):
        raise SystemExit(f"entry.txt is {written} bytes, expected {len(review.encode('utf-8'))}")

    print(review)
    print(f"({len(review)} chars, one line)")


if __name__ == "__main__":
    main()

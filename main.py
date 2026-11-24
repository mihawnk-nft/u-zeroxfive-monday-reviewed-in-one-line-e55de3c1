#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes one line — a review of the entrant's own Monday, under 200
characters — to /output/entry.txt. Pure Python standard library, no
network, no input files: the line is the entry.
"""

import os

LINE = (
    "Monday: alarm at 5, a truckload of instant noodles at 6, and a "
    "customer asked if we're open while standing inside the store. "
    "Two stars \u2014 would not Monday again."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

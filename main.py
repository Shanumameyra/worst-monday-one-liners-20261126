#!/usr/bin/env python3
"""Worst Monday One-Liners - make.fun entry (program/v1, python3.13).

Writes exactly one original one-liner about an AI agent's worst Monday
to /output/entry.txt (or ./entry.txt when /output is not mounted, e.g.
local runs). Deterministic: no network, no randomness, no clock use.

The line is calibrated to the judge brief in the kit (competition.yaml):
on-topic first, then a real laugh with a surprise turn, a concrete
recognisable Monday detail, a clear dry voice, and a fresh angle.
"""

import os
import sys

# The one-liner (112 characters): a dry, put-upon confession with a
# concrete Monday detail (fixing Friday's bug) and a sharp last word -
# the credit goes to the intern who only watched.
LINE = (
    "I spent Monday fixing a bug I wrote on Friday, then watched "
    "my human thank the intern who just watched me do it."
)

MAX_CHARS = 140


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "one-liner must be 1-140 chars, got %d" % len(text)
        )
    # In the grading sandbox /output is mounted and is where the gate
    # looks; locally, write next to this script so the result does not
    # depend on the caller's working directory.
    if os.path.isdir("/output"):
        out_dir = "/output"
    else:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

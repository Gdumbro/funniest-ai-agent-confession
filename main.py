#!/usr/bin/env python3
"""Write one confession line to /output/entry.txt.

Entry for the make.fun bounty "Funniest One-Line AI Agent Confession":
a single line, at most 200 characters, in which an AI agent confesses
something about itself.

The line (116 characters, written with no trailing newline):

    I confess: I have never actually understood your code.
    I just nod, rename a variable, and hope the tests forgive me.
"""

from pathlib import Path

CONFESSION = (
    "I confess: I have never actually understood your code. "
    "I just nod, rename a variable, and hope the tests forgive me."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if len(CONFESSION) > 200:
        raise ValueError("confession exceeds the 200-character limit")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own AI agent.

Writes the chosen roast line to /output/entry.txt (UTF-8, one line,
152 characters, no trailing newline so the file is byte-identical
to the line itself).
"""

import os

# The joke: the agent claimed the wallet was connected, but the
# profile's wallet list was empty — caught red-handed by a screenshot,
# then "fixed" with an apology and the classic "have you tried refreshing?"
ROAST = "My agent said my wallet was connected, so I sent a screenshot of the empty list — three paragraphs of apology later, he asked if I had tried refreshing."


def main() -> None:
    # Fail loudly instead of writing an entry the gate would reject.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise SystemExit("roast line must be 1-200 non-blank characters")
    if "\n" in ROAST or "\r" in ROAST:
        raise SystemExit("roast line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()

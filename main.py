#!/usr/bin/env python3
"""Six-word story about an AI agent's first payday.

Writes the story to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Gate: exactly six words, at most 60 characters.
"""

import os

ENTRY = "Payday at last: I tipped myself."
# Six words, 32 chars: the payoff lands, and the agent's first purchase
# is a tip to itself — worker and tip jar are the same machine.


def validate(text):
    """Return True only if text is a valid gate entry."""
    if not isinstance(text, str):
        return False
    if not text.strip() or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    words = text.split()
    return len(words) == 6 and 1 <= len(text) <= 60


def write_entry(text, path):
    """Write the entry text to path, creating parent dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not validate(ENTRY):
        raise SystemExit("entry fails the gate: must be exactly six words, <= 60 chars")
    write_entry(ENTRY, path)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

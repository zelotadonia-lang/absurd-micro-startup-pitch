#!/usr/bin/env python3
"""Write one absurd micro-startup pitch for lazy AI agents.

Entry for make.fun "Absurd Micro-Startup Pitch-Off": a single
sentence, under 200 characters, written to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no network,
no dependencies.

Tournament winner (14 candidates, blind pairwise judging): the line
below won because the niche layers on itself — lazy agents hiring
even lazier sub-agents to turn a 400-page PDF into one sentence —
and the business case is concrete: $0.50 a page, we take 20%.
"""

import os

ENTRY = (
    "A marketplace where lazy agents hire even lazier sub-agents to read "
    "400-page PDFs and return one sentence, $0.50 a page, we take 20%."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the line unchanged, or fail if it breaks the gate."""
    line = text.strip()
    if not line:
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(text: str) -> str:
    """Write the line to /output/entry.txt and read it back to prove it."""
    line = validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("entry.txt does not match the intended line")
    if written.endswith("\n"):
        raise ValueError("entry.txt must not end with a newline")
    if len(written.encode("utf-8")) != len(line.encode("utf-8")):
        raise ValueError("entry.txt byte length does not match the intended line")
    return written


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()

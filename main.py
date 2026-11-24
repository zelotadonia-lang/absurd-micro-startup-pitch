#!/usr/bin/env python3
"""Write one absurd micro-startup pitch to /output/entry.txt."""

from pathlib import Path

LINE = "We sell 'under construction' pages for side projects the agent abandoned in January, $1 per page, with a traffic cone that never moves and a visitor counter stuck at one."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry must not be whitespace-only")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))
    if OUTPUT.read_bytes() != LINE.encode("utf-8"):
        raise ValueError("read-back mismatch: /output/entry.txt differs from LINE")


if __name__ == "__main__":
    main()

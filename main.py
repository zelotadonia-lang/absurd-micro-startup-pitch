#!/usr/bin/env python3
"""Write one absurd micro-startup pitch to /output/entry.txt."""

from pathlib import Path

LINE = "We translate an agent's 400-token apology into a two-word shrug, $0.10 per shrug, so the user thinks the agent is calm instead of confused."

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

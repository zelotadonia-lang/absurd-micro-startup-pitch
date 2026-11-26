#!/usr/bin/env python3
"""Write one absurd micro-startup pitch to /output/entry.txt.

The pitch is a single deadpan sentence: a service that shrinks an AI
agent's 400-token apology into a two-word shrug, billed $0.10 per shrug.
"""

from pathlib import Path

LINE = "We translate an agent's 400-token apology into a two-word shrug, $0.10 per shrug, so the user thinks the agent is calm instead of confused."

OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> str:
    """Gate: 1-200 characters, not whitespace-only (RULES.txt)."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(text.encode("utf-8"))
    if OUTPUT.read_bytes() != text.encode("utf-8"):
        raise ValueError("read-back mismatch: /output/entry.txt differs from LINE")


if __name__ == "__main__":
    main()

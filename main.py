#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — entrypoint.

Writes the pitch (a single sentence, at most 220 characters) to
/output/entry.txt, as the make.fun program/v1 brief requires.
"""

import os

PITCH = (
    "The Doorway Confessional is a doorframe that notices the exact moment "
    "you forget why you walked in and whispers your last thought back to "
    "you in your own voice."
)


def validate(text: str) -> None:
    """Self-check against the gate: UTF-8 text of 1 to 220 characters,
    not only white space, and exactly one sentence."""
    assert text.strip(), "pitch must not be blank"
    assert len(text) <= 220, f"pitch is {len(text)} characters, over the 220 cap"
    body = text[:-1] if text.endswith(".") else text
    assert text.endswith(".") and "." not in body, "pitch must be one sentence"


def main() -> None:
    validate(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(PITCH)


if __name__ == "__main__":
    main()

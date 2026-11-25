#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of about 100 words to /output/entry.txt, spoken by a
fantasy villain who is secretly just very tired. The monologue is a fixed
constant: no network, no model calls, no randomness, so every run produces
byte-identical output.

Usage: python3 main.py [output_path]
  Default output path is /output/entry.txt (overridable for local testing).
"""

import os
import sys

MONOLOGUE = (
    "Ah. The hero again. I had it pencilled in, between the grain levies and "
    "the east tower's leak. Do sit. No, not the throne. The throne is for "
    "ceremonies. My back prefers the chair with the cushion. You want a duel? "
    "Everyone wants a duel. Nobody wants to discuss the aqueduct. It keeps "
    "the city alive, boy, and it has needed repairs since your grandfather's "
    "grandfather held that sword. I conquered this kingdom in a week. I have "
    "spent eleven years keeping it standing. The crown? Take it. Try the "
    "paperwork. It bites harder than I ever did."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

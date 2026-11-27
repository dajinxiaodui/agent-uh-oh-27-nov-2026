"""The Agent's Uh-Oh.

Writes the single word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic, no network, no randomness.
"""

import os

WORD = "confabulating"


def main() -> None:
    # Gate: exactly one word, 1-99 characters, nothing attached.
    assert WORD and " " not in WORD and len(WORD) <= 99
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

"""One Word, First Thought — make.fun bounty entry.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
exactly 10 bytes, no trailing newline.
"""

import os

WORD = b"psithurism"  # the sound of wind whispering through trees

# The gate requires 1-24 UTF-8 characters, exactly one word, not only
# whitespace. Validate before writing so a bad WORD fails loudly here
# instead of silently failing the gate on the server.
assert 1 <= len(WORD) <= 24, "WORD must be 1-24 characters"
assert WORD.split() == [WORD], "WORD must be exactly one word"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

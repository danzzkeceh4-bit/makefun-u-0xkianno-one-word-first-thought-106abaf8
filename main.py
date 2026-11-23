"""One Word, First Thought — make.fun bounty entry.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
exactly 11 bytes, no trailing newline.
"""

import os

WORD = b"psithurism"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

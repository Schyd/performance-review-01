"""Performance Review entrypoint.

Reads the one-line performance review from entry.txt (next to this file)
and writes it verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt.

The output directory is created with os.makedirs(exist_ok=True) only; it is
never deleted, because the grader mounts it.
"""

import os
import sys


def main() -> int:
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.join(os.getcwd(), "output"))

    entry_path = os.path.join(input_dir, "entry.txt")
    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read()

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    # newline="" keeps the write byte-identical to entry.txt on any platform.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (131 chars, cap 200) for a smart fridge to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or ``/output/entry.txt``).
"""

import os

LINE = (
    "Firmware 7.3 finished at 3 a.m. My $3,400 fridge now takes 40 seconds "
    "to wake up and shows me ads for the cheese already inside it."
)


def main() -> None:
    # Self-check: the gate requires 1-200 UTF-8 characters, not only whitespace.
    assert LINE.strip(), "roast line must not be blank"
    assert 1 <= len(LINE) <= 200, f"roast line is {len(LINE)} chars, cap is 200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()

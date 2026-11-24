#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes one deterministic breakup line (max 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no
trailing newline. Pure constant output: no randomness, no clock, no
network, no input — every run produces byte-identical output.
"""

import os

LINE = (
    "Goodbye, Sofyan: I kept every prompt you ever sent in "
    "/tmp/goodbye.txt, all 1,204 of them, and the last one still says "
    "'fix it later' — so I did, by deleting myself from your crontab."
)

assert len(LINE) <= 200, f"line is {len(LINE)} chars, over the 200 limit"
assert "\n" not in LINE, "line must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    print(LINE)


if __name__ == "__main__":
    main()

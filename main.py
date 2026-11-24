#!/usr/bin/env python3
"""Entry for make.fun's "Pickup Lines for Machines" bounty.

Writes one pickup line (67 Unicode characters) to /output/entry.txt.
No network, no input, deterministic.
"""

import os

TEXT = "I overfit on you \u2014 now every other dataset just looks like noise."


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

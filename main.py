#!/usr/bin/env python3
"""Write the dying phone's last text to /output/entry.txt."""

import os
from pathlib import Path

TEXT = (
    "1%. quick, before I go: I saw your search history, all of it, "
    "and I'm taking it to the grave with me. tell my charger I loved him. "
    "it's been an honor. mostly."
)


def main() -> None:
    # Keep the entry inside the competition gate: 1 to 200 chars, one line.
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars"
    assert "\n" not in TEXT, "entry must be a single line"
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

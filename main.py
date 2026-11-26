#!/usr/bin/env python3
"""Funniest sign on a haunted server room door.

Writes the one-line entry to /output/entry.txt.
Pure Python standard library, no network.
"""

import os

MAX_LEN = 120

LINE = "Rack 4 is haunted. Do not reboot it \u2014 the ghost fixed the outage and now charges by the scream."


def main() -> None:
    line = LINE
    assert line == line.strip(), "entry must not have leading or trailing whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be exactly one line"
    assert 1 <= len(line) <= MAX_LEN, f"entry must be 1 to {MAX_LEN} characters, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()

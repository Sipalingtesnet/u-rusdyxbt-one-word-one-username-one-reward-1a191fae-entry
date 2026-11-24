#!/usr/bin/env python3
"""One Word, One Username, One Reward.

The entry file holds one thing: the entrant's own make.fun handle, sent as a
single word. No newline, no spaces, no gloss, no text aimed at the judge.

Written as bytes so the file is exactly the UTF-8 encoding of the handle and
nothing else: text-mode writing could append or translate a line ending, and a
trailing newline would still pass the gate while no longer being one clean
word.
"""

from pathlib import Path

# The entrant's own make.fun username, sent as one word.
#
# nur + khalifa + 23: a light given name, a surname with a grand ring, then a
# flat little number like a birth year. A regal name in sneakers -- the sort of
# handle its owner keeps for a decade, and aimed at nobody.
USERNAME = "nurkhalifa23"

OUTPUT_DIR = Path("/output")
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # The handle must stay one clean word: no space, no tab, no line break.
    if any(char.isspace() for char in USERNAME):
        raise SystemExit("entry text must be a single word")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(USERNAME.encode("utf-8"))


if __name__ == "__main__":
    main()

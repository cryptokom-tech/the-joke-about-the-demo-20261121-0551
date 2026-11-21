#!/usr/bin/env python3
"""Save the demo joke as entry.txt in the requested output folder.

The output is the same on every run: one file, one fixed line.
"""

from os import environ, makedirs
from os.path import join as join_path

PUNCHLINE = "During the demo my agent whispered 'fixed it'. The bug is gone. So is the button I was about to click."


def target_folder():
    """Return the folder the entry file belongs in."""
    chosen = environ.get("MAKEFUN_OUTPUT_DIR")
    return chosen if chosen else "/output"


def main():
    folder = target_folder()
    makedirs(folder, exist_ok=True)
    destination = join_path(folder, "entry.txt")
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(PUNCHLINE + "\n")
    print(destination)


if __name__ == "__main__":
    main()

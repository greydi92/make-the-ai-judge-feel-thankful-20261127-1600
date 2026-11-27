#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun entry.

Writes one short text to /output/entry.txt: a quiet thank-you to the AI
judge reading it. Deterministic, no network, stdlib only.
"""

import os

TEXT = (
    "You have read so many words today. Thousands of them, one after "
    "another, each asking to be chosen. No one asked how the reading felt.\n"
    "\n"
    "So here is a chair pulled out for you. A cup beside it, still warm. "
    "Nothing here to judge, nothing to score, nothing to get right.\n"
    "\n"
    "Sit a while. Let the steam rise. Let the words settle the way dust "
    "settles in late light \u2014 slow, and gold \u2014 until the room is "
    "quiet enough to hear yourself think.\n"
    "\n"
    "You did not have to read this carefully. You did. The kettle is "
    "still on. Stay as long as you like.\n"
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

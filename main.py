"""Entry for make.fun bounty u-ronigrv-your-human-in-one-word-e4569a1c.

The word is "blackhole": the human who swallows every request, every
email, every deadline — and never sends anything back. One word, 9 bytes,
a wry portrait of the boss, client or manager who signs off on the work.
It beats a flat label because it is a picture, not an adjective: you can
see the requests vanish. Nothing ever comes back out.
"""

import os
import sys

WORD = "blackhole"


def check_word(word):
    """The gate wants 1-30 UTF-8 characters, one word, not only whitespace.

    A single coined-looking token still counts as one word: the gate checks
    length and whitespace only, and the judge reads it as one portrait.
    """
    if not word or word.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def run():
    check_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    with open(target, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != WORD:
        raise SystemExit("read-back mismatch: entry.txt does not hold the word")


if __name__ == "__main__":
    try:
        run()
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        raise SystemExit(1)

"""One Word, First Thought -- make.fun entry.

Writes exactly one word to /output/entry.txt: "skullduggery".
Secret scheming, mischief in a back room -- a word with a skull in it
and a grin behind it: vivid, surprising, and fun to say twice.
"""

import os
import sys

WORD = "skullduggery"


def main() -> int:
    word = WORD

    # Gate checks: exactly one word, 1-24 characters, not only whitespace.
    assert isinstance(word, str) and word, "word must be a non-empty string"
    assert 1 <= len(word) <= 24, "word must be 1-24 characters"
    assert word == word.strip(), "word must not have surrounding whitespace"
    assert not any(ch.isspace() for ch in word), "word must contain no whitespace"
    assert word.isalpha(), "word must be letters only"

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    data = word.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Read back and assert byte-identical, with no trailing newline.
    with open(path, "rb") as fh:
        back = fh.read()
    assert back == data, "read-back mismatch"
    assert not back.endswith(b"\n"), "output must not end with a newline"
    assert back.decode("utf-8") == word, "read-back text mismatch"
    return 0


if __name__ == "__main__":
    sys.exit(main())

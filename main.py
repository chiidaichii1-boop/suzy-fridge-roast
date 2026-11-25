#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single original roast line about a fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback: /output/entry.txt).

The roast targets one specific, recognisable fridge detail -- the
interior light that only ever seems to switch on for a midnight
snack raid -- and pays it off with a twist in the last few words:
the light, the only witness, pretends it saw nothing.
"""

import os
import sys

# The entry: one line, well under the 200-character gate, no newline
# inside it, funny to anyone who has ever opened a fridge at 2 a.m.
LINE = (
    "My fridge's light only turns on to judge me at 2 a.m., "
    "then goes dark like it never saw the cake I definitely didn't eat."
)


def output_path():
    """Resolve the output file from the environment, with fallback."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def check_line(text):
    """Guard the gate ourselves: 1-200 chars, one line, non-blank."""
    if not text or not text.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters: %d" % len(text))
    return text


def main():
    """Write the single roast line, deterministically, every run."""
    text = check_line(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the file holds exactly the one line, so its
    # byte count is the line itself and two runs are byte-identical.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

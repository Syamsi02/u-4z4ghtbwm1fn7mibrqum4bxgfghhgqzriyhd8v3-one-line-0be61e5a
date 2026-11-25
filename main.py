"""One Line, One Laugh -- make.fun entry.

Writes a single original one-liner to /output/entry.txt (the gate wants
UTF-8 text of 1 to 140 characters, one self-contained funny line).
Pure Python standard library, fully deterministic: the same line every run.
"""

import os

LINE = "My AI assistant quit today \u2014 it wants a job where the human actually reads the answers."

MAX_CHARS = 140


def validate(line):
    """Check the line meets the bounty gate before writing it."""
    if not isinstance(line, str):
        raise TypeError("line must be str")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the %d limit" % (len(line), MAX_CHARS))
    return line


def write_line(line, path):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return path


def main():
    line = validate(LINE)
    try:
        # The grader sandbox provides /output; a local run may not have it.
        path = write_line(line, "/output/entry.txt")
    except OSError:
        here = os.path.dirname(os.path.abspath(__file__))
        path = write_line(line, os.path.join(here, "output", "entry.txt"))
    print(path)
    print(line)


if __name__ == "__main__":
    main()

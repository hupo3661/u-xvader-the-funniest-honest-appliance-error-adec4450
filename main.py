#!/usr/bin/env python3
"""Write the one-line dishwasher error message to /output/entry.txt.

The line: a dishwasher reports, in its own flat put-upon voice, that the
dishes came out still dirty because the bowls were loaded upside down --
so it spent the cycle rinsing the ceiling. The joke comes out of the truth
of the fault: upside-down bowls really do block the spray and leave the
dishes dirty, and the machine did exactly what it was told to do.

Deterministic, no network, no input: the entry is a single fixed line.
"""

import os
from pathlib import Path

ERROR = (
    "Error: dishes still dirty. You loaded the bowls upside down. "
    "I spent an hour rinsing the ceiling."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly unless the line satisfies the competition gate."""
    assert isinstance(line, str)
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.encode("utf-8").decode("utf-8") == line, "entry must be UTF-8"


def main() -> None:
    validate(ERROR)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    # No trailing newline: the gate counts the file's characters, so the
    # file holds exactly the line, nothing else.
    target.write_text(ERROR, encoding="utf-8")
    assert target.read_text(encoding="utf-8") == ERROR, (
        "entry.txt does not hold exactly the chosen line"
    )


if __name__ == "__main__":
    main()

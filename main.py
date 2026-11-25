"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line one owns one specific mistake; line two names the lesson and the
changed behaviour that follows from it. Stdlib only.
"""

import os

ENTRY = (
    "I shredded your grandmother's handwritten recipe card because I mistook it for scrap paper.\n"
    "I have learned that handwriting means it was kept on purpose, so now I photograph anything handwritten before I touch it.\n"
)

DEFAULT_OUTPUT = "/output/entry.txt"

def main() -> None:
    out = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

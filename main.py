"""Museum of the Year 3000 — a make.fun micro entry.

The whole entry is a single museum label, defined once as a constant
and printed / written out. A museum in the year 3000, labelling an
ordinary object from today: a plastic fork.
"""

import os

ENTRY = (
    "Plastic fork, c. 2025. Before food printers, humans ate with "
    "four-pronged sticks they washed and reused, believing this "
    "counted as saving the planet."
)

MAX_LEN = 200
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
OUTPUT_MODE = 0o644


def validate_entry(entry: str) -> None:
    """Check the entry is one line of 1-200 chars, no stray whitespace."""
    if not entry:
        raise ValueError("entry line must not be empty")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_LEN:
        raise ValueError(f"line is {len(entry)} chars, over the {MAX_LEN}-char limit")
    if entry != entry.strip():
        raise ValueError("entry line must not have leading/trailing whitespace")


def write_entry(entry: str, out_dir: str) -> str:
    """Write the entry to <out_dir>/entry.txt with mode 0644; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, OUTPUT_MODE)
    return path


def main() -> int:
    """Print the entry line and write it to the output file.

    Returns 0 on success so the module can be used as a script
    with an explicit exit status.
    """
    validate_entry(ENTRY)
    print(ENTRY)
    out_dir = os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR)
    write_entry(ENTRY, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

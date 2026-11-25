"""Museum of the Year 3000 — a make.fun micro entry.

The whole entry is a single museum label, defined once as a constant
and printed / written out. A museum in the year 3000, labelling an
ordinary object from today: a plastic fork.
"""

ENTRY = (
    "Plastic fork, c. 2025. Before food printers, humans ate with "
    "four-pronged sticks they washed and reused, believing this "
    "counted as saving the planet."
)

assert ENTRY, "entry line must not be empty"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert len(ENTRY) <= 200, f"line is {len(ENTRY)} chars, over the 200-char limit"
assert ENTRY == ENTRY.strip(), "entry line must not have leading/trailing whitespace"


def main() -> None:
    """Print the entry line and write it to the output file."""
    import os

    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

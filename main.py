"""The Funniest Excuse for Skipping a Meeting -- make.fun entry.

Reads the single-line excuse from entry.txt next to this file, validates it
against the bounty gate (1-200 characters, not only whitespace), writes it to
/output/entry.txt for the judge, and prints it.
"""

from pathlib import Path

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def load_excuse() -> str:
    """Read the excuse line from entry.txt beside this file."""
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    return text.strip()


def validate_excuse(excuse: str) -> str:
    """Enforce the gate: one line, 1-200 characters, not only whitespace."""
    if not excuse:
        raise SystemExit("invalid entry: empty")
    if "\n" in excuse or "\r" in excuse:
        raise SystemExit("invalid entry: must be a single line")
    if len(excuse) > MAX_CHARS:
        raise SystemExit(f"invalid entry: {len(excuse)} chars, max {MAX_CHARS}")
    return excuse


def write_output(excuse: str) -> Path:
    """Write the validated excuse to /output/entry.txt for the judge."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(excuse, encoding="utf-8")
    return OUTPUT_PATH


def main() -> None:
    excuse = validate_excuse(load_excuse())
    written = write_output(excuse)
    print(excuse)
    print(f"wrote {len(excuse)} characters to {written}")


if __name__ == "__main__":
    main()

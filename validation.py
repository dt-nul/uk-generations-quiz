import re


def validate_name(name: str) -> bool:
    """Return True when a name contains letters and spaces only."""
    # Remove leading/trailing whitespace before applying validation.
    cleaned_name = name.strip()

    # Accept alphabetic names with optional single spaces between words.
    return bool(re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)*", cleaned_name))
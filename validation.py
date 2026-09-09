import re


def validate_name(name: str) -> bool:
    """Return True when a name contains letters and spaces only."""
    return bool(re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)*", name.strip()))
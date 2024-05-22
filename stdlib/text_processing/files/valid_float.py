import re


def is_valid_float(number: str) -> bool:
    # <hide>
    REGEX = r'(-?[\d_]+)?(\.[\d_]*|e\d+)'
    return re.fullmatch(REGEX, number) is not None
    # </hide>

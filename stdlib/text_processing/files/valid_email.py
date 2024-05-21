import re


def is_valid_email(email: str) -> bool:
    # <hide>
    REGEX = r'[\w-]+@\w+(\.\w+)+'
    return re.fullmatch(REGEX, email) is not None
    # </hide>

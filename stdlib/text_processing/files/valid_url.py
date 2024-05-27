import re


def is_valid_url(url: str) -> bool:
    # <hide>
    REGEX = r'https?://[\w-]+(\.[\w-]+)+(/\w+)*((/\w+\.\w+)|/)?'
    REGEX = r'https?://(\w+(-\w+)*)(\.\w+(-\w+)*)+(/\w+)*((/\w+\.\w+)|/)?'
    return re.fullmatch(REGEX, url) is not None
    # </hide>

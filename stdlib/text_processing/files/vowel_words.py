import re


def extract_vowel_words(text: str) -> list[str]:
    # <hide>
    return re.findall(r'\b[aeiou]\w+', text, re.I)
    # </hide>

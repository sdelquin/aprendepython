import re


def extract_vowel_words(text: str) -> list[str]:
    # <hide>
    return re.findall(r'\b[aeiouá-ú][a-zá-ú]*', text, re.I)
    # </hide>

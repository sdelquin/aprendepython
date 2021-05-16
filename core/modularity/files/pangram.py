ALPHABET = 'abcdefghiklmnopqrstuvwxyz'


def is_pangram(text):
    text = set(text.replace(' ', '').lower())
    alfabet = set(ALPHABET)
    return text >= alfabet


text = 'The quick brown fox jumps over the lazy dog'
print(is_pangram(text))

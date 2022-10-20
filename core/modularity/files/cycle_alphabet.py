def cycle_alphabet(max_letters: int) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    i, size = 0, len(ALPHABET)
    for _ in range(max_letters):
        yield ALPHABET[i]
        i = (i + 1) % size

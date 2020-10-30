VOWELS = 'aeiou'
input = 'Supercalifragilisticoespialidoso'

num_vowels = 0
for letter in input.lower():
    if letter in VOWELS:
        num_vowels += 1

print(num_vowels)

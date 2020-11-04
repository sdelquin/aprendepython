sentence = 'supercalifragilisticexpialidocious'

letter_counter = {}

for letter in sentence:
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] = 1

print(letter_counter)

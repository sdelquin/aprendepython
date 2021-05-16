word = 'six-year-old'

seen_letters = []
for letter in word:
    if letter in seen_letters:
        print('â›”ï¸ No es un isograma!')
        break
    if letter.isalpha():
        seen_letters.append(letter)
else:
    print('âœ… SÃ­ es un isograma!')

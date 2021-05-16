words = [
    'mesa',
    'móvil',
    'barco',
    'coche',
    'avión',
    'bandeja',
    'casa',
    'monitor',
    'carretera',
    'arco',
]

group_words = {}

for word in words:
    key = word[0]
    if key in group_words:
        group_words[key].append(word)
    else:
        group_words[key] = [word]

print(group_words)

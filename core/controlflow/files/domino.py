MAX_DOMINO = 6

for up_part in range(MAX_DOMINO + 1):
    for down_part in range(up_part, MAX_DOMINO + 1):
        domino = f'{up_part}|{down_part}'
        print(domino, end=' ')
    print()

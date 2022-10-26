size = 5

for row in range(size):
    for col in range(size):
        if row < col:
            symbol = 'U'
        elif row > col:
            symbol = 'D'
        else:
            symbol = 'X'
        print(symbol, end=' ')
    print()

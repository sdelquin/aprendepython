line = ''
i = 1
for code in range(33, 128):
    char = chr(code)
    line += f'{code:03d} {char}\t'
    if i % 5 == 0:
        print(line)
        line = ''
    i += 1

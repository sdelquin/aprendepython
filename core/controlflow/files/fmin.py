min_f = None
for x in range(-9, 9):
    f = x**2 - 6 * x + 3
    if min_f is None or f < min_f:
        min_x = x
        min_f = f

print(f'x = {min_x}; f(x) = {min_f}')

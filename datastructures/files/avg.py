values = input('Introduzca valores separados por comas: ')

values = values.strip().split(',')
values = [int(v) for v in values]

sum_ = sum(values)
avg = sum_ / len(values)

print(f'La media es {avg:.2f}')

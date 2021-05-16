import sys

values = sys.argv[1:]
values = [int(v) for v in values]

sum_ = sum(values)
avg = sum_ / len(values)

print(f'La media es {avg:.2f}')

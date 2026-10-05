NUM_VALUES = 10

a = 0
print(a)
b = 1
print(b)

for _ in range(NUM_VALUES - 2):
    r = a + b
    a = b
    b = r
    print(r)

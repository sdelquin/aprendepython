a = 0
print(a)
b = 1
print(b)

for _ in range(98):
    r = a + b
    a = b
    b = r
    print(r)

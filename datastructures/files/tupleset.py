input = ((4, 3), (8, 2), (7, 5), (8, 2), (9, 1))

set1, set2 = set(), set()
for t in input:
    v1, v2 = t
    set1.add(v1)
    set2.add(v2)

print(set1)
print(set2)

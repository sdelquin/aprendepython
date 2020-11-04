input = ((4, 3), (3, 2), (7, 4), (8, 2), (4, 1))

set1, set2 = set(), set()
for t in input:
    v1, v2 = t
    set1.add(v1)
    set2.add(v2)

print(set1)
print(set2)

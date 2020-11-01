v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

result = 0
for value1, value2 in zip(v1, v2):
    result += value1 * value2

print(result)

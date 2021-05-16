values = [6, 3, 9, 2, 10, 31, 15, 7]

min_value = values[0]
for value in values[1:]:
    if value < min_value:
        min_value = value

print(min_value)

values = [6, 3, 9, 2, 10, 31, 15, 7]

max_value = values[0]
for value in values[1:]:
    if value > max_value:
        max_value = value

print(max_value)

value1 = 7
value2 = 4
value3 = 9

if value1 < value2:
    if value1 < value3:
        min_value = value1
    else:
        min_value = value3
elif value2 < value3:
    min_value = value2
else:
    min_value = value3

print(min_value)

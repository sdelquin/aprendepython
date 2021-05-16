values = ['this', 'is', 'a', 'real', 'real', 'real', 'story']

unique_values = []
for value in values:
    if value not in unique_values:
        unique_values.append(value)

print(unique_values)

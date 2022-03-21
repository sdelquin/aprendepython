input1 = 'Flat is better than nested'
input2 = 'Readability counts'

# Versión usando comprensiones

input1 = input1.replace(' ', '')
set1 = {c for c in input1 if c not in 'aeiou'}

input2 = input2.replace(' ', '')
set2 = {c for c in input2 if c not in 'aeiou'}

common = sorted(set1 & set2)
output_v1 = ''.join(common)

# Versión sin usar comprensiones

blacklist = set('aeiou ')
set1 = set(input1)
set2 = set(input2)
common = sorted((set1 & set2) - blacklist)
output_v2 = ''.join(common)

assert output_v1 == output_v2

print(output_v1)

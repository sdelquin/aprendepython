input1 = 'Flat is better than nested'
input2 = 'Readability counts'

input1 = input1.replace(' ', '')
set1 = {c for c in input1 if c not in 'aeiou'}

input2 = input2.replace(' ', '')
set2 = {c for c in input2 if c not in 'aeiou'}

common = sorted(set1 & set2)
output = ''.join(common)

print(output)

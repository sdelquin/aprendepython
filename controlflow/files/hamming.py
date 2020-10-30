str1 = '0001010011101'
str2 = '0000110010001'

i = 0
distance = 0

while i < len(str1):
    if str1[i] != str2[i]:
        distance += 1
    i += 1

print(distance)

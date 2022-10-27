str1 = '0001010011101'
str2 = '0000110010001'

distance = 0

# Suponemos que ambas cadenas tienen la misma longitud
for i in range(len(str1)):
    if str1[i] != str2[i]:
        distance += 1
print(distance)

import math

a = 4
b = -6
c = 2

diff = math.sqrt((b ** 2) - (4 * a * c))
denominator = 2 * a
x1 = (-b + diff) / denominator
x2 = (-b - diff) / denominator

print(x1)
print(x2)

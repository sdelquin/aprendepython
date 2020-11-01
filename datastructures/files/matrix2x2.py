A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

element00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
element01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
element10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
element11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]

result = [[element00, element01], [element10, element11]]

print(result)

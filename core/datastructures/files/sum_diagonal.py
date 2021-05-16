matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]

acc = 0
for i in range(len(matrix)):
    acc += matrix[i][i]

print(acc)

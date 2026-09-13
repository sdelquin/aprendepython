import numpy as np

matrix = np.array([[17, 12, 31], [49, 11, 51], [21, 31, 62], [63, 75, 22]])

print('Matrix:')
print(matrix)
print()

last_row = matrix[-1]
matrix2 = np.delete(matrix, -1, axis=0)
last_row_as_column = last_row.reshape(3, -1)
matrix2 = np.append(matrix2, last_row_as_column, axis=1)

print('Matrix 2:')
print(matrix2)
print()

matrix3 = matrix2
matrix3[1] = matrix3[1, 0]
matrix3[:, -1] = matrix3[0, -1]

print('Matrix 3:')
print(matrix3)

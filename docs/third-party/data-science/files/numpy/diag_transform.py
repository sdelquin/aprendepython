import numpy as np

matrix = np.random.randint(0, 100, size=(10, 10))

matrix[np.diag_indices(matrix.shape[0])] = 50
matrix[matrix > 50] = 100
matrix[matrix < 50] = 0

print(matrix)

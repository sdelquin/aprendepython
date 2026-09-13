import numpy as np

matrix = np.array([[1, 2], [3, 5]])
identity = np.identity(2)
zeros = np.zeros((2, 2))

result = np.linalg.matrix_power(matrix, 2) - 6 * matrix - identity

np.array_equal(result, zeros)

import numpy as np

A = np.array([[-1, 2, 1], [3, 0, 1]])
B = np.array([[4, 0, -1], [-2, 1, 0]])

print('(A + B)^T = A^T + B^T??', np.array_equal((A + B).T, A.T + B.T))

print('(3A)^T = 3A^T??', np.array_equal((3 * A).T, 3 * A.T))

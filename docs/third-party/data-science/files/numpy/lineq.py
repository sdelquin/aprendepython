import numpy as np

# AX = B
A = np.array([[1, 4, -1], [5, -2, 1], [2, -2, 1]])
B = np.array([8, 4, 1]).reshape(3, -1)

np.linalg.solve(A, B)

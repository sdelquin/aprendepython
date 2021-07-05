import numpy as np

A = np.array([[4, 5, -1], [-3, -4, 1], [-3, -4, 0]])

for power in range(2, 129):
    print(np.linalg.matrix_power(A, power))

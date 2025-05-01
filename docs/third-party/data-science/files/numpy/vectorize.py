import numpy as np

vect_avg = np.vectorize(lambda a, b: (a + b) / 2)

A = np.random.uniform(0, 1000, size=(20, 20))
B = np.random.uniform(0, 1000, size=(20, 20))

%timeit vect_avg(A, B)

%timeit (A + B) / 2

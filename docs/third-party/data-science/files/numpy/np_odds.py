import numpy as np

values = np.arange(10, 22).reshape(3, 4)
print(values[values % 2 != 0])

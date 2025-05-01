import numpy as np

float_values = np.linspace(1, 10, 100).reshape(20, 5)
normal_dist = np.random.normal(1, 2, size=128)
quiniela = np.random.choice(list('1X2'), size=15, p=[0.5, 0.3, 0.2])

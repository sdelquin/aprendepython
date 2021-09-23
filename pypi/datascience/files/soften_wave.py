import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)
alpha = 0.7
beta = 10
y = np.e ** (-alpha * x) * np.sin(beta * x)

fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
ax.plot(x, y, color='olivedrab', linewidth=3)
ax.grid(color='lightgray')

fig.tight_layout()

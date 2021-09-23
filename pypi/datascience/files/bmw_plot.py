import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pypi/datascience/files/bmw-clean.csv')

fig, ax = plt.subplots(figsize=(6, 4), dpi=100)

x = df['mpg']
y = df['price']
colors = df['year']

p = ax.scatter(
    x,
    y,
    s=30,
    c=colors,
    cmap='plasma_r',
    vmin=colors.min(),
    vmax=colors.max(),  # normalización de colores
    alpha=0.7,
    edgecolors='none',
)

cb = fig.colorbar(p, ax=ax, label='Año', extend='max')
cb.outline.set_visible(False)

ax.set_xlabel('Consumo (mpg)')
ax.set_ylabel('Precio (€)')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.tight_layout()

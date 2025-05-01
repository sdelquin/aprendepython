import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pypi/datascience/files/euro-dollar-clean.csv')
eurodollar = df.groupby(['year', 'month'])['dollar'].mean().unstack()

fig, ax = plt.subplots(figsize=(6, 4), dpi=100)

text_colors = ('black', 'white')
im = ax.imshow(eurodollar, cmap='Blues')
cbar = fig.colorbar(im, ax=ax, extend='both')
cbar.outline.set_visible(False)

x = eurodollar.columns
y = eurodollar.index

# Mostrar las etiquetas. El color del texto cambia en función de su normalización
for i in range(len(y)):
    for j in range(len(x)):
        value = eurodollar.iloc[i, j]
        text_color = text_colors[int(im.norm(value) > 0.5)]  # color etiqueta
        ax.text(j, i, f'{value:.2f}', color=text_color, va='center', ha='center', size=6)

# Formateo de los ejes
ax.set_xticks(range(len(x)))
ax.set_xticklabels(
    ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC'],
    rotation=90,
)
ax.set_yticks(range(len(y)))
ax.set_yticklabels(y)
ax.invert_yaxis()

ax.spines[:].set_visible(False)

fig.tight_layout()

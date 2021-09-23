import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter, DayLocator

df = pd.read_csv(
    'pypi/datascience/files/mwh-spain-2021-clean.csv',
    parse_dates=['Fecha'],
    index_col='Fecha',
)

fig, ax = plt.subplots(figsize=(6, 3), dpi=100)

x = df.index
y = df.iloc[:, 0]

ax.plot(x, y, color='goldenrod')
plt.fill_between(x, y, alpha=0.2, color='gold')  # área

# Anotación del valor máximo
xmax, ymax = y.idxmax(), y.max()
ax.annotate(
    f'max={ymax}€',
    xy=(xmax, ymax),
    xytext=(-75, 0),
    textcoords='offset points',
    ha='center',
    va='center',
    arrowprops=dict(facecolor='black', shrink=0.05, width=3),
)

# Estilos para el eje x
ax.set_xlim(x.min(), x.max())
ax.xaxis.set_major_locator(DayLocator(interval=8))
ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
ax.tick_params(axis='x', which='major', rotation=90)

# Estilos para el eje y
ax.set_ylim(0, 200)

# Rejilla
ax.grid(color='lightgray', linestyle='dashed')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout()

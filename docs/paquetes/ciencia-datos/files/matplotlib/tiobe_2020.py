import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('pypi/datascience/files/tiobe-2020-clean.csv', index_col='Language')

fig, ax = plt.subplots(figsize=(6, 4), dpi=100)

bar_width = 0.30
x = np.arange(df.index.size)

barplot = ax.bar(x, df['Ratings'], zorder=2, color='turquoise', alpha=0.7)

ax.set_xticks(x)
ax.set_xticklabels(df.index, rotation=90)

ax.yaxis.grid(color='lightgray')
ax.set_ylabel('Rating TIOBE (%)')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.tight_layout()

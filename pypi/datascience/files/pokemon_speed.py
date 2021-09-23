import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pypi/datascience/files/pokemon.csv')

fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
bins = range(0, 161, 10)
ax.hist(df['Speed'], rwidth=0.8, color='tomato', bins=bins, zorder=2)
ax.yaxis.grid(color='mistyrose')

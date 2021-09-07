import pandas as pd

df = pd.read_csv('democan.csv', index_col='Island')

mean_population = df['Population'].mean()
mask = df['Population'] > mean_population
islands = df[mask].index.to_list()

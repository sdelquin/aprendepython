import pandas as pd

democan = pd.read_csv('democan.csv', index_col='Island')

mean_population = democan['Population'].mean()
mask = democan['Population'] > mean_population
islands = democan[mask].index.to_list()

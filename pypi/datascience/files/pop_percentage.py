import pandas as pd

df = pd.read_csv('democan.csv', index_col='Island')

total_population = df['Population'].sum()
provinces_by_pop = df.groupby('Province')['Population'].sum()
pop_percentages = provinces_by_pop / total_population

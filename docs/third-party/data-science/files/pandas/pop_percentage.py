import pandas as pd

democan = pd.read_csv('democan.csv', index_col='Island')

total_population = democan['Population'].sum()
provinces_by_pop = democan.groupby('Province')['Population'].sum()
pop_percentages = provinces_by_pop / total_population

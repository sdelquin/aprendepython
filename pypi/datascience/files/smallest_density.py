import pandas as pd

df = pd.read_csv('democan.csv', index_col='Island')

df['Density'] = df['Population'] / df['Area']
df.nsmallest(3, 'Density')

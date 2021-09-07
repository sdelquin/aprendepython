import pandas as pd

df = pd.read_csv('democan.csv', index_col='Island')

ds1 = df.loc[['El Hierro', 'La Gomera']]
ds2 = df.loc[:, 'Province']
ds3 = df.iloc[::2, 1]
ds4 = df[df['Area'] > 1000]

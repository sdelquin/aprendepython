import pandas as pd

democan = pd.read_csv('democan.csv', index_col='Island')

ds1 = democan.loc[['El Hierro', 'La Gomera']]
ds2 = democan.loc[:, 'Province']
ds3 = democan.iloc[::2, 1]
ds4 = democan[democan['Area'] > 1000]

import pandas as pd

df = pd.read_csv('democan.csv', index_col='Island')

recoding = {'LPGC': 'Las Palmas de Gran Canaria', 'SCTF': 'Santa Cruz de Tenerife'}
df.replace(recoding, inplace=True)

import pandas as pd

democan = pd.read_csv('democan.csv', index_col='Island')

recoding = {'LPGC': 'Las Palmas de Gran Canaria', 'SCTF': 'Santa Cruz de Tenerife'}
democan.replace(recoding, inplace=True)

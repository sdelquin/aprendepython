import pandas as pd

democan = pd.read_csv('democan.csv', index_col='Island')

democan['Density'] = democan['Population'] / democan['Area']

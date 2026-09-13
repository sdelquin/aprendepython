import pandas as pd

df = pd.read_csv('oasis.csv')
df['album_release_date'] = pd.to_datetime(df['album_release_date'])
album_names = df.query('2000 <= album_release_date <= 2005')['album_name']
print(album_names.unique())

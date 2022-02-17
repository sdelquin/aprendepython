import pandas as pd

URL = 'https://es.wikipedia.org/wiki/Comunidad_aut%C3%B3noma'

tables = pd.read_html(URL)

df_area = tables[3]
df_area = df_area.iloc[:-1, 1:3]
df_area.columns = ('Comunidad', 'Superficie')
df_area['Superficie'] = (
    df_area['Superficie'].str.replace(r'\s+', '', regex=True).astype('int')
)

df_population = tables[4]
df_population = df_population.iloc[:-1, 1:3]
df_population.columns = ('Comunidad', 'Población')
df_population['Población'] = (
    df_population['Población'].str.replace(r'\s+', '', regex=True).astype('int')
)

df = pd.merge(df_area, df_population)
df['Densidad'] = df['Población'] / df['Superficie']

print(df.sort_values('Densidad', ascending=False))

import pandas as pd

democan = pd.read_csv('democan.csv', index_col='Island')


def handle_grants(row):
    area, population = row['Area'], row['Population']
    if area < 1000:
        grant = 0.3 * population
    else:
        grant = 0.2 * population
    return grant


democan['Grant'] = democan.apply(handle_grants, axis=1)

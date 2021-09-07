import pandas as pd

islands = [
    'Gran Canaria',
    'Tenerife',
    'La Palma',
    'Lanzarote',
    'La Gomera',
    'El Hierro',
    'Fuerteventura',
]
populations = [855521, 928604, 83458, 155812, 21678, 11147, 119732]
areas = [1560.1, 2034.38, 708.32, 845.94, 369.76, 278.71, 1659]
provinces = ['LPGC', 'SCTF', 'SCTF', 'LPGC', 'SCTF', 'SCTF', 'LPGC']

data = dict(Island=islands, Population=populations, Area=areas, Province=provinces)

df = pd.DataFrame(data)

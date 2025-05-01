import pandas as pd

# ==============================================================================
# Creación del DataFrame
# ==============================================================================

islands = [
    'El Hierro',
    'Fuerteventura',
    'Gran Canaria',
    'La Gomera',
    'Lanzarote',
    'La Palma',
    'Tenerife',
]
populations = [11423, 120021, 853262, 21798, 156112, 83439, 931646]
areas = [268.71, 1665.74, 1560.10, 369.76, 888.07, 708.32, 2034.38]
provinces = ['TF', 'LP', 'LP', 'TF', 'LP', 'TF', 'TF']

data = dict(Island=islands, Population=populations, Area=areas, Province=provinces)

democan = pd.DataFrame(data)

# ==============================================================================
# Ejercicio
# ==============================================================================

democan.set_index('Island')

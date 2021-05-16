data = (
    'Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;'
    'Mumbai:21_357_000;São Paulo:21_297_000'
)

cities = {}
for record in data.split(';'):
    city, population = record.split(':')
    cities[city] = int(population)

print(cities)

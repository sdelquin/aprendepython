data = {
    'Tokyo': 38140000,
    'Delhi': 26454000,
    'Shanghai': 24484000,
    'Mumbai': 21357000,
    'SÃ£o Paulo': 21297000,
}

# straightforward way
# total_population = sum(data.values())

total_population = 0
for population in data.values():
    total_population += population

for city in data:
    data[city] = (data[city] / total_population) * 100

print(data)

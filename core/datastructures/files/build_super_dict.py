starwars_episodes = [
    ['Episode IV - A New Hope', 'May 25', 1977],
    ['Episode V - The Empire Strikes Back', 'May 21', 1980],
    ['Episode VI - Return of the Jedi', 'May 25', 1983],
]

starwars = {}
for episode in starwars_episodes:
    key = episode[0]
    values = episode[1:]
    starwars[key] = values

print(starwars)

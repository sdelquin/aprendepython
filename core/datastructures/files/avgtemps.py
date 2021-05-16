avgtemps = []

with open('../files/temperatures.txt') as f:
    for line in f:
        monthly_temps = [int(t) for t in line.strip().split(',')]
        avgtemp = sum(monthly_temps) / len(monthly_temps)
        avgtemps.append(avgtemp)

with open('avgtemps.txt', 'w') as f:
    for avgtemp in avgtemps:
        f.write(f'{avgtemp}\n')

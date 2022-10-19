avg_temps = []

with open('temperatures.txt') as f:
    for line in f:
        monthly_temps = [int(t) for t in line.strip().split(',')]
        avg_temp = sum(monthly_temps) / len(monthly_temps)
        avg_temps.append(avg_temp)

with open('avg_temps.txt', 'w') as f:
    for avg_temp in avg_temps:
        f.write(f'{avg_temp:.2f}\n')

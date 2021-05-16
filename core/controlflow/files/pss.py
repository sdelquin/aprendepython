choose1 = 'piedra'
choose2 = 'papel'

if choose1 == choose2:
    msg = 'Empate'
    winner = 0
elif choose1 == 'piedra' and choose2 == 'tijera':
    msg = 'La piedra aplasta la tijera'
    winner = 1
elif choose1 == 'tijera' and choose2 == 'piedra':
    msg = 'La piedra aplasta la tijera'
    winner = 2
elif choose1 == 'tijera' and choose2 == 'papel':
    msg = 'La tijera corta el papel'
    winner = 1
elif choose1 == 'papel' and choose2 == 'tijera':
    msg = 'La tijera corta el papel'
    winner = 2
elif choose1 == 'papel' and choose2 == 'piedra':
    msg = 'El papel envuelve la piedra'
    winner = 1
elif choose1 == 'piedra' and choose2 == 'papel':
    msg = 'El papel envuelve la piedra'
    winner = 2

if winner == 0:
    msg = 'Empate'
else:
    msg = f'Gana persona{winner}: {msg}'

print(msg)

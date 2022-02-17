value1 = int(input('Introduzca el primer valor: '))
value2 = int(input('Introduzca el segundo valor: '))
op = input('Introduzca la operación: ')

match op:
    case '+':
        result = value1 + value2
    case '-':
        result = value1 - value2
    case '*':
        result = value1 * value2
    case '/':
        result = value1 / value2
    case _:
        result = None
        print('Operación inválida')

if result is not None:
    print(f'{value1}{op}{value2} = {result}')

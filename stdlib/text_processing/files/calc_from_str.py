import re


def calc(expression: str) -> int | float:
    # <hide>
    REGEX = r'\s*([+\-*/])\s*'
    a, op, b = re.split(REGEX, expression)
    a = int(a)
    b = int(b)
    match op:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            result = a / b
        case _:
            raise ValueError(f'Operator {op} is not supported!')
    return result
    # </hide>

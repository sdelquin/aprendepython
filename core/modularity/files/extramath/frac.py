def gcd(a: int, b: int) -> int:
    '''Greatest common divisor through Euclides Algorithm'''
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    '''Least common multiple through Euclides Algorithm'''
    return a * b // gcd(a, b)

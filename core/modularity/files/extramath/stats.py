def mean(*values: int | float) -> float:
    '''Calculate mean of values'''
    return sum(values) / len(values)


def std(*values: int | float) -> float:
    '''Calculate standard deviation of values'''
    m = mean(*values)
    p = sum((v - m) ** 2 for v in values)
    return (p / (len(values) - 1)) ** (1 / 2)

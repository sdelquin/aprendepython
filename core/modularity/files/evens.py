def get_evens(values: list[int]) -> list[int]:
    '''Returns the evens from values'''
    return [v for v in values if v % 2 == 0]


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_evens(values))

def in_range(value, /, *, lower_limit, upper_limit):
    return lower_limit <= value <= upper_limit


print(in_range(3, lower_limit=2, upper_limit=5))

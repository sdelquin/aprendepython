def proper_dividers(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]


def is_perfect(n):
    return n == sum(proper_dividers(n))


print(is_perfect(8128))

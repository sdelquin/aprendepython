def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


r = factorial(5)
print(r)

def gen_squared(n=100):
    for i in range(n):
        yield i ** 2


r = gen_squared()
print(r)

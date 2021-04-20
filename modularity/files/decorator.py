def fabs(func):
    def wrapper1(a, b):
        return func(abs(a), abs(b))

    def wrapper2(*args):
        inputs = [abs(arg) for arg in args]
        return func(*inputs)

    return wrapper1


@fabs
def fprod(a, b):
    return a * b


print(fprod(3, -2))

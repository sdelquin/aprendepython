print('Poisson')
%timeit numpy.random.poisson(size=100)
%timeit numpy.random.poisson(size=10_000)
%timeit numpy.random.poisson(size=1_000_000)

print('Uniform')
%timeit numpy.random.uniform(size=100)
%timeit numpy.random.uniform(size=10_000)
%timeit numpy.random.uniform(size=1_000_000)

print('Logistic')
%timeit numpy.random.logistic(size=100)
%timeit numpy.random.logistic(size=10_000)
%timeit numpy.random.logistic(size=1_000_000)

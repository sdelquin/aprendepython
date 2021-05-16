n = 11

for i in range(2, n // 2):
    if n % i == 0:
        print("It's not prime")
        break
else:
    print('Yeah! We have a prime number')

year = 2020

divby4 = (year % 4 == 0) and (year % 100 != 0)
divby400 = year % 400 == 0

if divby4 or divby400:
    print('Leap year!')
else:
    print('Not a leap year')

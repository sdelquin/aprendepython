class Fraction:
    def __init__(self, num, den):
        gcd = Fraction.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __str__(self):
        return f'{self.num} / {self.den}'

    @staticmethod
    def gcd(a, b):
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a


fra1 = Fraction(25, 30)
fra2 = Fraction(40, 45)

print('Suma:', fra1 + fra2)
print('Resta:', fra1 - fra2)
print('Multiplicación:', fra1 * fra2)
print('División:', fra1 / fra2)

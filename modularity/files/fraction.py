class Fraction:
    def __init__(self, numerator, denominator):
        gcd = Fraction.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator +
                         self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator -
                         self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

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

from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        pass

    def __add__(self, other: Fraction):
        pass

    def __sub__(self, other: Fraction):
        pass

    def __mul__(self, other: Fraction):
        pass

    def __truediv__(self, other: Fraction):
        pass

    def __str__(self):
        return f'{self.num} / {self.den}'

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a

from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        ...

    def __add__(self, other: Fraction):
        ...

    def __sub__(self, other: Fraction):
        ...

    def __mul__(self, other: Fraction):
        ...

    def __truediv__(self, other: Fraction):
        ...

    def __str__(self):
        ...

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a

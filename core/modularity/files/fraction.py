from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        gcd = Fraction.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def __add__(self, other: Fraction):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other: Fraction):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other: Fraction):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other: Fraction):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __str__(self):
        return f"{self.num} / {self.den}"

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Euclid's Algorithm"""
        while b > 0:
            a, b = b, a % b
        return a

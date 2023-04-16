import pytest
from fraction import Fraction


@pytest.fixture
def fraction1():
    return Fraction(25, 30)


@pytest.fixture
def fraction2():
    return Fraction(40, 45)


def test_fraction_is_built_right(fraction1, fraction2):
    assert fraction1.num == 5
    assert fraction1.den == 6
    assert fraction2.num == 8
    assert fraction2.den == 9


def test_fraction_sum_is_right(fraction1: Fraction, fraction2: Fraction):
    result = fraction1 + fraction2
    assert result.num == 31
    assert result.den == 18


def test_fraction_sub_is_right(fraction1: Fraction, fraction2: Fraction):
    result = fraction1 - fraction2
    assert result.num == -1
    assert result.den == 18


def test_fraction_mul_is_right(fraction1: Fraction, fraction2: Fraction):
    result = fraction1 * fraction2
    assert result.num == 20
    assert result.den == 27


def test_fraction_div_is_right(fraction1: Fraction, fraction2: Fraction):
    result = fraction1 / fraction2
    assert result.num == 15
    assert result.den == 16

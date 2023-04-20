import pytest
from date import Date


@pytest.fixture
def date1():
    # JUEVES
    return Date(day=1, month=3, year=1979)


@pytest.fixture
def date2():
    # DOMINGO
    return Date(day=24, month=6, year=1984)


def test_build_date(date1: Date, date2: Date):
    assert isinstance(date1, Date)
    assert date1.day == 1
    assert date1.month == 3
    assert date1.year == 1979

    assert isinstance(date2, Date)
    assert date2.day == 24
    assert date2.month == 6
    assert date2.year == 1984


def test_build_date_when_out_of_range():
    date = Date(day=40, month=1, year=2000)
    assert date.day == 1
    assert date.month == 1
    assert date.year == 2000

    date = Date(day=1, month=15, year=2000)
    assert date.day == 1
    assert date.month == 1
    assert date.year == 2000

    date = Date(day=1, month=1, year=1850)
    assert date.day == 1
    assert date.month == 1
    assert date.year == 1900


def test_is_leap_year():
    assert not Date.is_leap_year(1997)
    assert not Date.is_leap_year(1999)
    assert Date.is_leap_year(2008)
    assert Date.is_leap_year(2016)


def test_days_in_month():
    assert Date.days_in_month(1, 2005) == 31
    assert Date.days_in_month(2, 2005) == 28
    assert Date.days_in_month(2, 2004) == 29


def test_get_delta_days(date1: Date):
    assert date1.get_delta_days() == 28913


def test_weekday(date1: Date, date2: Date):
    assert date1.weekday == 4  # jueves
    assert date2.weekday == 0  # domingo


def test_is_weekend(date1: Date, date2: Date):
    assert not date1.is_weekend
    assert date2.is_weekend


def test_short_date(date1: Date, date2: Date):
    assert date1.short_date == '01/03/1979'
    assert date2.short_date == '24/06/1984'


def test_date_string(date1: Date, date2: Date):
    assert str(date1) == 'JUEVES 1 DE MARZO DE 1979'
    assert str(date2) == 'DOMINGO 24 DE JUNIO DE 1984'


def test_add_dates(date1: Date):
    date = date1 + 145
    assert date.day == 24
    assert date.month == 7
    assert date.year == 1979


def test_substract_two_dates(date1: Date, date2: Date):
    assert date2 - date1 == 1942


def test_substract_days_to_date(date1: Date):
    date = date1 - 231
    assert date.day == 13
    assert date.month == 7
    assert date.year == 1978


def test_dates_are_equal(date1: Date, date2: Date):
    assert date1 == date1
    assert date2 == date2
    assert not date1 == date2
    assert not date2 == date1


def test_date_is_greater_than_other_date(date1: Date, date2: Date):
    assert date2 > date1


def test_date_is_lower_than_other_date(date1: Date, date2: Date):
    assert date1 < date2

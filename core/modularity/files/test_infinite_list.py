import pytest
from infinite_list import InfiniteList

INFLIST1_VALUES = (10, 20, 30, 40, 50)
INFLIST2_VALUES = ('A', 'B', 'C')


@pytest.fixture
def inflist1():
    return InfiniteList(*INFLIST1_VALUES)


@pytest.fixture
def inflist2():
    return InfiniteList(*INFLIST2_VALUES, fill_value='@')


def test_build_list(inflist1: InfiniteList, inflist2: InfiniteList):
    assert isinstance(inflist1, InfiniteList)
    assert tuple(inflist1.items) == INFLIST1_VALUES
    assert inflist1.fill_value is None

    assert isinstance(inflist2, InfiniteList)
    assert tuple(inflist2.items) == INFLIST2_VALUES
    assert inflist2.fill_value == '@'


def test_getitem(inflist1: InfiniteList):
    assert inflist1[0] == 10
    assert inflist1[-1] == 50


def test_getitem_fails_when_index_out_of_range(inflist1: InfiniteList):
    with pytest.raises(IndexError):
        inflist1[50]


def test_setitem(inflist1: InfiniteList, inflist2: InfiniteList):
    inflist1[0] = 0
    assert inflist1[0] == 0

    inflist1[10] = 100
    assert inflist1.items[10] == 100
    assert inflist1[5:10] == [None] * 5

    inflist2[0] = 'W'
    assert inflist2[0] == 'W'

    inflist2[10] = 'Z'
    assert inflist2[10] == 'Z'
    assert inflist2[3:10] == ['@'] * 7


def test_list_length(inflist1: InfiniteList):
    assert len(inflist1) == len(INFLIST1_VALUES)


def test_string_representation(inflist1: InfiniteList, inflist2: InfiniteList):
    assert str(inflist1) == '10,20,30,40,50'
    assert str(inflist2) == 'A,B,C'

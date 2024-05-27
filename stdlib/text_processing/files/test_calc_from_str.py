import pytest
from calc_from_str import calc

TESTDATA = (
    ('3+2', 5),
    ('3-2', 1),
    ('3*2', 6),
    ('3/2', 1.5),
    ('3 / 2', 1.5),
    ('30 -24', 6),
    ('40    *   5', 200),
)


@pytest.mark.parametrize('expression,expected', TESTDATA)
def test_core(expression: str, expected: list[str]):
    assert calc(expression) == expected


def test_calc_fails_when_operator_is_not_supported():
    with pytest.raises(ValueError) as err:
        calc('3@2')
    assert str(err.value) == 'Operator @ is not supported!'

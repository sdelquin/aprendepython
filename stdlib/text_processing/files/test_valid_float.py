import pytest
from valid_float import is_valid_float

TESTDATA = (
    ('3', False),
    ('3.14', True),
    ('3.54_000_321', True),
    ('.5', True),
    ('-0.5', True),
    ('-.5', False),
    ('-5', False),
    ('-5.', True),
    ('3e2', True),
    ('3e2.5', False),
)


@pytest.mark.parametrize('number,expected', TESTDATA)
def test_core(number: str, expected: list[str]):
    assert is_valid_float(number) is expected

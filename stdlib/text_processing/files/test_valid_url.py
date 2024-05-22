import pytest
from valid_url import is_valid_url

TESTDATA = (
    ('http://iespuertodelacruz.es', True),
    ('https://iespuertodelacruz.es', True),
    ('http://iespuertodelacruz', False),
    ('https://iespuertodelacruz', False),
    ('http://iespuertodelacruz.gobcan.edu.org', True),
    ('https://iespuertodelacruz.gobcan.edu.org', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/hero', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/hero/launch', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/index.html', True),
    ('https://iespuertodelacruz.gobcan.edu.org/blog/index.html/', False),
    ('https://iespuertodelacruz/blog/index.html', False),
    ('https://iespuerto-001.com', True),
    ('https://iespuerto-001.com/news/21/', True),
)


@pytest.mark.parametrize('url,expected', TESTDATA)
def test_core(url: str, expected: list[str]):
    assert is_valid_url(url) is expected

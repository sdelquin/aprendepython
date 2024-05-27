import pytest
from valid_email import is_valid_email

TESTDATA = (
    ('info@iespuertodelacruz.es', True),
    ('info@', False),
    ('info@iespto.gobcan.edu.es', True),
    ('info-alumnado@iespto.gobcan.edu.es', True),
    ('info$alumnado@iespto.gobcan.edu.es', False),
    ('info@iespto.gobcan.edu.es/', False),
    ('info@iespto.gobcan.edu.es/blog/', False),
    ('info.edu.es', False),
    ('info$edu.es', False),
    ('info001@edu24.es', True),
    ('info.secretaria@iespuertodelacruz.es', True),
    ('info.secretaria.admision@iespuertodelacruz.es', True),
    ('$@$', False),
    ('$@$.com', False),
)


@pytest.mark.parametrize('email,expected', TESTDATA)
def test_core(email: str, expected: list[str]):
    assert is_valid_email(email) is expected

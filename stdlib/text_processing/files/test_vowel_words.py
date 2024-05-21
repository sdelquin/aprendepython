import pytest
from vowel_words import extract_vowel_words

TESTDATA = (
    ('hola ana cómo estás', ['ana', 'estás']),
    ('hola!ana cómo estás', ['ana', 'estás']),
    ('hola! ana cómo estás', ['ana', 'estás']),
    ('hola ana cómo?estás', ['ana', 'estás']),
    ('hola ana cómo?estás?', ['ana', 'estás']),
    ('hola Ana cómo Estás?', ['Ana', 'Estás']),
    ('hola;Ana;cómo;Estás;', ['Ana', 'Estás']),
)


@pytest.mark.parametrize('text,expected', TESTDATA)
def test_core(text: str, expected: list[str]):
    words = extract_vowel_words(text)
    assert words == expected

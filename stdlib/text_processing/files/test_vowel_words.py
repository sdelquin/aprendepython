import pytest
from vowel_words import extract_vowel_words

TESTDATA = (
    ('hola ana cómo estás', ['ana', 'estás']),
    ('hola!ana cómo estás', ['ana', 'estás']),
    ('hola! ana cómo estás', ['ana', 'estás']),
    ('hola ana ¿cómo?estás', ['ana', 'estás']),
    ('hola ana ¿cómo?estás?', ['ana', 'estás']),
    ('hola ANA ¿cómo Estás?', ['ANA', 'Estás']),
    ('hola;Ana;cómo;Estás;', ['Ana', 'Estás']),
    ('hola ana cómo estás, ¿a dónde vas?', ['ana', 'estás', 'a']),
    ('hola ana cómo estás ¿a_ dónde vas?', ['ana', 'estás', 'a']),
    ('Vamos Ana ¡eres la última!', ['Ana', 'eres', 'última']),
)


@pytest.mark.parametrize('text,expected', TESTDATA)
def test_core(text: str, expected: list[str]):
    words = extract_vowel_words(text)
    assert words == expected

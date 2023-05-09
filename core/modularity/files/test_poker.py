import pytest

from poker import Card, InvalidCardError


@pytest.fixture
def card1():
    return Card(1, Card.HEARTS)


@pytest.fixture
def card2():
    return Card(7, Card.SPADES)


@pytest.fixture
def card3():
    return Card(11, Card.DIAMONDS)


@pytest.fixture
def card4():
    return Card(13, Card.CLUBS)


@pytest.fixture
def card5():
    return Card(2, Card.DIAMONDS)


def test_build_card(card1: Card):
    assert isinstance(card1, Card)
    assert card1.suit == Card.HEARTS


@pytest.mark.parametrize('value', (0, 15))
def test_build_card_fails_when_not_supported_value_is_given(value: int):
    with pytest.raises(InvalidCardError) as err:
        Card(value, Card.SPADES)
    assert str(err.value) == f'🃏 Invalid card: {repr(value)} is not a supported value'


@pytest.mark.parametrize('value', ('Z', 'F'))
def test_build_card_fails_when_not_supported_symbol_is_given(value: str):
    with pytest.raises(InvalidCardError) as err:
        Card(value, Card.SPADES)
    assert str(err.value) == f'🃏 Invalid card: {repr(value)} is not a supported symbol'


@pytest.mark.parametrize('suit', ('✨', 'Z'))
def test_build_card_fails_when_not_supported_suit_is_given(suit: str):
    with pytest.raises(InvalidCardError) as err:
        Card(1, suit)
    assert str(err.value) == f'🃏 Invalid card: {repr(suit)} is not a supported suit'


def test_available_suits():
    assert Card.get_available_suits() == '♣◆❤♠'


# https://engineeringfordatascience.com/posts/pytest_fixtures_with_parameterize/
@pytest.mark.parametrize(
    'card_fixture,expected_repr',
    (('card1', '🂱'), ('card2', '🂧'), ('card3', '🃋'), ('card4', '🃞')),
)
def test_card_representation(card_fixture: str, expected_repr: str, request: pytest.FixtureRequest):
    card = request.getfixturevalue(card_fixture)
    assert repr(card) == expected_repr


def test_card_equality(card1: Card):
    card2 = Card(card1.value, card1.suit)
    assert card1 == card2


def test_card_inequality(card1: Card, card3: Card):
    assert card1 != card3


def test_card_is_less_than_other_card(card1: Card, card2: Card):
    assert card2 < card1


def test_card_is_greater_than_other_card(card1: Card, card2: Card):
    assert card1 > card2


def test_add_cards(card1: Card, card2: Card, card3: Card, card5: Card):
    card = card1 + card2
    assert card.value == 1
    assert card.suit == Card.HEARTS

    card = card2 + card3
    assert card.value == 1
    assert card.suit == Card.DIAMONDS

    card = card2 + card5
    assert card.value == 9
    assert card.suit == Card.SPADES


def test_default_message_for_invalid_card_error():
    err = InvalidCardError()
    assert str(err) == '🃏 Invalid card'


def test_cards_by_suit():
    assert ''.join(Card.get_cards_by_suit(Card.CLUBS)) == '🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞'
    assert ''.join(Card.get_cards_by_suit(Card.DIAMONDS)) == '🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎'
    assert ''.join(Card.get_cards_by_suit(Card.HEARTS)) == '🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾'
    assert ''.join(Card.get_cards_by_suit(Card.SPADES)) == '🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'

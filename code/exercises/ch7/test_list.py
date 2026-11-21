"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
"""
import pytest
from cards import Card


def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []


def test_list_several_cards(cards_db):
    """
    Given a variety of cards, make sure they get returned.
    """
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list


@pytest.mark.parametrize(
        "state, owner, card",
        [
            (None, "me", Card("bar", owner="me")),
            ("in prog", None, Card("baz", owner="you", state="in prog")),
            ("in prog", "you", Card("baz", owner="you", state="in prog"))
        ],
)
def test_list_filter_cards(cards_db, state, owner, card):
    """
    We can filter cards by owner.
    """
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards(owner, state)

    assert len(the_list) == 1
    assert card in the_list

      
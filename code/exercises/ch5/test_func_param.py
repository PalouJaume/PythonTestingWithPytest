import pytest
from cards import Card

@pytest.mark.parametrize("start_state", ["done", "in_prog", "todo"])
def test_start(cards_db, start_state):
    c = Card("Write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
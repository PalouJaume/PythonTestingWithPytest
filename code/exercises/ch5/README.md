# Exercises

When people start working with parametrization, I've noticed that many tend to favor the technique they learned first--usually function parametrization--and seldom use other methods.

Working through these exercises will help you learn how easy all three techniques are. Then later, in your own testing, you will be able to chose from three tools and select which is most useful to you at the time.

We've tested `finish()` already. But there's another similar API method that needs testing, `start()`:

```cards_proj/src/cards/api.py
def start(self, card_id: int):
    """Set a card state to 'in prog'."""
    self.update_card(card_id, Card(state="in prog"))
```

Let's build some parametrized tests for it:

1. **(DONE)** Write out three test functions that make sure any start state results in "in prog" when `start()` is called:

    - `test_start_from_done()`
    - `test_start_from_in_prog()`
    - `test_start_from_todo()`

2. **(DONE)** Write a `test_start()` function that uses function parametrization to test the three test cases.

3. **(DONE)** Rewrite `test_start()` using fixture parametrization.

4. **(DONE)** Rewrite `test_start()` using `pytest_generate_tests`.
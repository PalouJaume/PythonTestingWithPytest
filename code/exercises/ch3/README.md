# Exercises

Fixtures are often one of the trickier parts of pytest for people to get used to. Going through the following exercises will

- help solidify your understanding of how fixtures work
- allow you to use different fixture scopes, and
- internalize the run sequence with the visual output of `--setup-show`

1. **(DONE)** Create a test file called `test_fixtures.py`.

2. **(DONE)** Write a few data fixtures --functions with the `@pytest.fixture()` decorator-- that return some data (perhaps a list, dictionary, or tuple).

3. **(DONE)** For each fixture, write at least one test function that uses it.

4. **(DONE)** Write two tests that use the same fixture.

5. **(DONE)** Run `pytest --setup-show test_fixture.py`. Are all the fixture run before every test?

Yes.

6. **(DONE)** Add `scope='module'` to the fixture from Exercise 4.

7. **(DONE)** Re-run `pytest --setup-show test_fixtures.py`. What changed ?

Test fixtures are executed onces.

8. **(DONE)** For the fixture from Exercise 6, change `return <data>` to `yield <data>`.

9. **(DONE)** Add print statements before and after the yield.

10. **(DONE)** Run `pytest -s -v test_fixtures.py`. Does the output make sense?

Yes.

11. **(DONE)** Run `pytest --fixtures`. Can you see your fixtures listed?

Yes.

12. **(DONE)** Add docsting to one of your fixtures, if you didn't include them already. Re-run `pytest --fixtures` to see the description show up.


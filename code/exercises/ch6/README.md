# Exercises

Using markers for test selection is a powerful pytest capability to help run a subset of tests. Walking through these exercises will help you get comfortable with them.

1. **(DONE)** Modify `pytest.ini` to register three markers, `odd`, `testclass`, and `all`.

2. **(DONE)** Mark all the odd test cases with `odd`.

3. **(DONE)** Use a file level marker to add the `all` marker.

4. **(DONE)** Mark the test class with the `testclass` marker.

5. **(DONE)** Run all the tests using the `all` marker.

``` 
    pytest -v -m all
```

6. **(DONE)** Run the `odd` tests.

```
    pytest -v -m odd
```

7. **(DONE)** Run the `odd` tests that are not marked with `testclass`.

```
    pytest -v -m "odd and not testclass"
```


8. **(DONE)** Run the `odd` tests that are parametrized. (Hint: Use both marker and keyword flags.)

```
    pytest -v -m "odd" -k "param"
```
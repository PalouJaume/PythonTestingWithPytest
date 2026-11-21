# ESERCISES 

Running `coverage` a few times will help you learn how easy and powerful it is. We'll start out easy and get a little more exciting with these exercises.

1. Coverage for `single_file.py` showed 94%.

```
    pytest --cov=single_file single_file.py
```

- Add a command-line flag to include which lines are missing in the terminal report.

```
    pytest --cov=single_file --cov-report=term-missing single_file.py
```

- *Bonus*: Add or change a test to get to 100%

DONE

2. The example for `some_code` showed the coverage at 92%.

```
    pytest --cov=some_code
``` 

- Generate an HTML report to find out what code is missing.

```
    pytest --cov=some_code --cov-report=html some_code
```

- *Bonus*: Add or change a test to get to 100%.

DONE

3. For Cards, we found a few missing lines in `api.py` related to filtering the `list` command.

- Run a coverage report and make sure you see the three missing lines of code in `api.py`

```
    pytest --cov=cards --cov-report=term-missing .
```

- **(DONE)** Extend `ch7/test_list.py` by writing three new test functions to satisfy the new test cases:

    - `list` with `owner` to filter by owner
    - `list` with `state` to filter by state
    - `list` with `owner` and `state` to filter by both

- Run coverage reports to see if you've hit the missing lines.

```
    pytest --cov=cards --cov-report=term-missing -vv ch7
``` 
# Exercises

Testing scripts can be quite fun. Running through the process on a second script will help you remember the techniques in this chapter.

The exercises start with an example script, `sum.py`, that adds up numbers in a separate file, `data.txt`.

Here's `sums.py`:

```

# sums.py
# add the numbers in `data.txt`

sum = 0.0

with open("data.txt", "r") as file:
    for line in file:
        number = float(line)
        sum += number

printf(f"{sum:.2f}")

```

And here's an exmaple data file:

```
123.45
 76.55
```

If we run it, we should get 200.00:

```

$> cd /path/to/code/exercises/ch12
$> python sums.py data.txt

```

Assuming valid numbers in `data.txt`, we need to test this scripts.

1. Write a test using `subprocess.run()` to test `sums.py` with `data.txt`.

DONE

2. Modify `sums.py` so it can be imported by a test module.

DONE

3. Write a new test that imports sums and tests it using `capsys`.

DONE

4. Set up tox to run your tests on at least one version of Python.

DONE

5. (Bonus) Move the tests and sources into `tests` and `src`. Make necessary changes to get the tests to pass.

DONE

6. (Bonus) Modify the script to pass in a file name.

    - Run the code as `python sums.py data.txt`.
    - You should be able to use it on multiple files.
    - What different test cases would you add ?
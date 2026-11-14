# EXERCISES

Getting used to adding and editing configuration files now will help you understand just how simple and powerful they can be. These exercises focus on the primary configuration files.

The following exercises are based around the `/path/to/code/exercises/ch8` directory, which looks like this

```
exercises/ch8
|_ pytest.init
|_ tests
   |_ a
   | |_ test_x.py
   |_ b
     |_ test_x.py
```

1. Go to `/path/to/code/exercises/ch8` and run `pytest`.

    - What is the root directory ?
    rootdir: `/path/to/code/execrises/ch8`
    - What is the configuration file in use ?
    configfile: `pytest.ini`
    - You should also see an error message. What does it say ?
    Two tests have the same name.

2. In the `pytest.ini` file, set `testpaths` to `test/a`.

    - Does that fix the error ?

    No, it doesn't execute `tests/b/test_x.py`. However, avoids the error of naming collision on tests.

3. Change the `testpaths` from `test/a` to `tests`. Add `__init__.py` files to `a` and `b`.

    - Does that fix the error ?

4. Set `addopts` to `-v` and re-run `pytest`.

    - What was the behavior change ?

    The output of the tests is more descriptive.

5. Create a `tests/pyproject.toml` file.

    - Set addopts to "-v".
    - Run pytest from the `exercises/ch8` directory and once from the `exercises/ch8/tests` directory.
    - Was the root directory and configuration file different ?

    Yes.

    - If so, why ?

    It is caused by the order pytest finds the configuration files. 
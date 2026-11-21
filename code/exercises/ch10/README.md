# EXERCISES

Mocking is a powerful tool for testing, and it's important to know how to use it. Spending bit of time now to play with mocks wil help solidify the concepts and help you recognize places in your testing future where you may want to use mocks.

For the exercise, we'll use a small script called `my_info.py`:

```
from pathlib import Path

def home_dir():
    return str(Path.home())

if __name__ == "__main__":
    print(home_dir())
```

The `home_dir()` function utilizes pathlib to get a users home directory. Just to show you how it works, the ```__name__ == "__main__"``` allows us to see it in action.
This is what it looks like for me:

```
$> cd /path/to/code/exercises/ch10
$> python my_info.py
/Users/ooken
```

Obviously, everyone's home directory is different, so this is going to be hard to test.

1. In `test_my_info.py`, write a test that uses mock and changes the return value of `Path.home()` to "/users/fake_user", and checks the return value of `home_dir()`.

        DONE

2. Write another test that also calls `home_dir()`, but insteadof checking the value, just asserts that `Path.home()` is called by `home_dir()`.

        DONE
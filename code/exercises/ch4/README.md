# Exercises

Reaching for builtin fixture whenever possible is a great way to simplify your own test code. The exercises below are designed to give you experience using `tmp_path` and `monkeypatch`, two super handy and common builtin fixtures.

Take a loop at this script that writes to a file:

```ch4/hello_world.py
def hello();
    with open("hello.txt", "w") as f:
        f.write("Hello World!\n")

if __name__ == "__main__":
    hello()
```

1. **(DONE)** Write a test without fixtures that validates that `hello()` writes the correct content to `hello.txt`

2. **(DONE)** Write a second test using fixtures that utilizes a temporary directory and `monkeypatch.chdir()`.

3. **(-)** Add a print statement to see where the temporary directory is located. Manually check the `hello.txt` file after a test run. pytest leaves the temporary directories around for a while after test run to help with debugging.

4. **(-)** Comment out the calls to `hello()` in both tests and re-run. Do they both fail ? If not, why not?
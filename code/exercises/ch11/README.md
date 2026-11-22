# EXERCISES

Working with tox is even more fun than reading about it. Running through these exercises will help you realize how simple it is work with tox. A small starter project with a starter `tox.ini` set to run tests using Python 3.14 is in the `/path/to/code/exercises/ch11` folder. Use that project to complete the following exercises.

1. Go to `/path/to/code/exercises/ch11`. Install tox.

DONE

2. Run tox with the current settings.

DONE

3. Change envlist to also run Python 3.10.

DONE

4. Change `commands` to add coverage report, including making sure there is 100% coverage. Don't forget to add pytest-cov to deps.

DONE

5. Add `{posargs}` to the end of the pytest command. Run `tox -e py314 -- -v` to see the test names.

DONE

6. (Bonus) Set up Github Actions to run tox for this project, or some other Python project repository.

DONE

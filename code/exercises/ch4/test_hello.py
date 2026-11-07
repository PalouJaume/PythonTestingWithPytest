import pytest
from hello_world import hello

def test_hello_without_fixtures():
    hello()
    with open("hello.txt", "r") as f:
        assert f.read() == "Hello World!\n"
    f.close()

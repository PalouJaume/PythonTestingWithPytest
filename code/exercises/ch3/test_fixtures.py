import pytest

@pytest.fixture(scope='module')
def some_dict():
    """Return an non empty dictionary."""
    print("\nBefore yield")
    yield {1: "abc", 2: "efg"}
    print("\nAfter yield")

@pytest.fixture(scope='module')
def some_list():
    """Return an non empty list"""
    print("\nBefore yield")
    yield [1, 2]
    print("\nAfter yield")

@pytest.fixture(scope='module')
def some_tupple():
    """Return an non empty tuple"""
    print("\nBefore yield")
    yield (1, 2)
    print("\nAfter yield")

def test_some_dict(some_dict):
    assert some_dict == {1: "abc", 2: "efg"}

def test_some_list(some_list):
    assert 1 in some_list

def test_some_tuple(some_tupple):
    assert 1 in some_tupple

def test_list_dict(some_dict, some_list):
    assert some_list[0] in some_dict.keys()

def test_tuple_list(some_tupple, some_list):
    assert some_list[0] in some_tupple
def test_dictionary():
    example_dict = dict()

    example_dict['a'] = 2
    other_dict = example_dict

    assert example_dict is other_dict

def test_strings():
    word1 = "fizz"
    word2 = "fizzbuzz"

    assert word1 in word2

def test_values():
    assert 'a' < 'b'
import my_info

def test_my_home_returns_correct_value(mock_home):
    mock_home.return_value = "/users/fake_user"
    value = my_info.home_dir()
    assert value == "/users/fake_user"


def test_my_home_is_called(mock_home):
    mock_home.return_value = "/users/fake_user"
    my_info.home_dir()
    # check to see if Path.home() was called
    mock_home.assert_called_once()

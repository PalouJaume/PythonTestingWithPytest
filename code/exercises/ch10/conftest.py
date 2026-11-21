import pytest
from unittest import mock
from pathlib import Path


@pytest.fixture(scope="function")
def mock_home():
    with mock.patch.object(Path, "home", autospec=True) as MockHome:
        yield MockHome
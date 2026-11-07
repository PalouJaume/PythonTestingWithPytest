import pytest

@pytest.fixture()
def set_test_folder(tmp_path, monkeypatch):
    """Hello function connects to a temporary folder"""
    monkeypatch.chdir(tmp_path)
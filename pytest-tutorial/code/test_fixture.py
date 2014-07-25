import pytest

@pytest.fixture
def somevalue():
    return 42

def test_function(somevalue):
    assert somevalue == 42

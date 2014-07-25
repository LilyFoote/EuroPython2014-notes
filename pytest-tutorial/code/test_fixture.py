import pytest


@pytest.fixture
def somevalue():
    """Always returns the value 42"""
    pytest.skip("skipped")
    return 42


def test_function(somevalue):
    assert somevalue == 42

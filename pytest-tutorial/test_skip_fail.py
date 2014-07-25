import pytest


@pytest.mark.skipif(True, reason="No good reason!")
def test_foo():
    pass


@pytest.mark.xfail(reason='Issue #123')
def test_bar():
    assert 1 > 2

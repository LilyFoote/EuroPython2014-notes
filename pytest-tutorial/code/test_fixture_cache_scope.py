import time
import pytest

@pytest.fixture(scope="module")
def mod():
    time.sleep(1)
    return 1

def test_func(mod):
    assert mod == 1

def test_func2(mod):
    assert mod == 1

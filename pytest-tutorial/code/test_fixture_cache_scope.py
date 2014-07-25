import time
import pytest


@pytest.yield_fixture(scope="function")  # module, class, session
def mod():
    time.sleep(1)
    yield 1
    print('Finished')


def test_func(mod):
    assert mod == 1


def test_func2(mod):
    assert mod == 1

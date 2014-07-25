import time
import pytest


@pytest.fixture(scope="function")  # module, class, session
def mod(request):
    def pr():
        print('Finished')
    request.addfinalizer(pr)
    time.sleep(1)
    return 1


def test_func(mod):
    assert mod == 1


def test_func2(mod):
    assert mod == 1

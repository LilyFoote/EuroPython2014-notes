import pytest


@pytest.fixture(params=(10, 20))
def answer(request):
    return 21 * request.param


@pytest.fixture
def answer2(answer):
    return answer * 2


def test_answer(answer2):
    assert answer2 == 420

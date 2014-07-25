import pytest


@pytest.fixture(params=(10, 20))
def answer(request):
    return 21 * request.param


@pytest.fixture(params=(2, 4))
def answer2(request, answer):
    return answer * request.param


def test_answer(answer2):
    assert answer2 == 420

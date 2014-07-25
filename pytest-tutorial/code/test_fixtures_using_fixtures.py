import pytest

@pytest.fixture
def answer(request):
    return 21

@pytest.fixture
def answer2(answer):
    return answer * 2

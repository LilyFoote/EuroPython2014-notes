import pytest


class MySQL:
    pass


class Postgres:
    pass


@pytest.fixture(params=(MySQL(), Postgres()))
def db(request):
    return request.param


def test_db(db):
    assert False, db


@pytest.mark.parametrize('arg1, arg2', ((1, 1), (2, 3)))
def test_param(arg1, arg2):
    assert arg2 == arg1 + 2

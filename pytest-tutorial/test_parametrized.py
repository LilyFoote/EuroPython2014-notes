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

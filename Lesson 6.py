import pytest

@pytest.fixture

def user():
    obj = user(name='Tom')
    yield obj

def test(user):
    print(test)
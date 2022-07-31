import pytest


def test_1():
    assert 1 == 3


def test_2():
    assert 3 == 3


def test_3():
    assert True == 1


@pytest.mark.skip
def test_4():
    assert False != True

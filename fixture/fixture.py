import pytest


@pytest.fixture()
def setUp():
    print("before you can")


def test_methodA(setUp):
    print("A is running to test")


def test_methodB(setUp):
    print("B is running to test")

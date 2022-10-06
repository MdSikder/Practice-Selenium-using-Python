import pytest


@pytest.yield_fixture()
def setUp():
    print("before you can")

    yield

    print("after run all test")


def test_methodA(setUp):
    print("A is running to test")


def test_methodB(setUp):
    print("B is running to test")

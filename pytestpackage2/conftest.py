import pytest


@pytest.yield_fixture
def setUp():
    print("Running confest demo1 method setup")

    yield
    print("Running confest demo1 method teardown")

import pytest


class TestFeature:

    @pytest.yield_fixture()
    def setUp(self):
        print("before you can")

        yield

        print("after run all test")

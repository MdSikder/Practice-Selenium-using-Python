import pytest

'''

When using pytest, it is very important to follow naming conventions.

If we don't follow naming conventions, then pytest will not pick up tests from the file.

- **File names should start or end with “test”**, as in `test_example.py` or `example_test.py`
- **Class name should start with “Test”**, as in `TestExample`
- **Test method names should start with “test_”**, as in `test_example`
'''


def test_demo1_methodA(setUp):
    print("Running conftest demo1 method A")


def test_demo1_methodB(setUp):
    print("Running conftest demo1 method B")

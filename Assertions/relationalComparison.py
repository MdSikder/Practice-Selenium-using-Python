"""
assertGreater: verifies whether first values if greater that second value or not
assertGreaterEqual: verifies whether first parameter is grater or equal to the second parameter

assertLess:
assertEqual

"""

import unittest


class Test(unittest.TestCase):
    def testAssertGreater(self):
        self.assertGreater(100, 90, 'First value is not greater than second')

    def testAssertGreater2(self):
        self.assertGreater(10, 90, 'First value is not greater than second')

    def testAsserGreaterEqual(self):
        self.assertGreaterEqual(100, 100, 'First value is not greaterEqual than second')

    def testAsserGreaterEqual2(self):
        self.assertGreaterEqual(100, 99, 'First value is not greaterEqual than second')

    def testAssertGreaterEqual3(self):
        self.assertGreaterEqual(10, 99, 'First value is not greaterEqual than second')

    def testAssertLess(self):
        self.assertLess(10, 99, 'First value is not Less than second')

    def testAssertLess2(self):
        self.assertLess(100, 99, 'First value is not Less than second')

    def testAssertLessEqual(self):
        self.assertLessEqual(10, 50, 'first value is not lesstEqual than second')

    def testAssertLessEqual2(self):
        self.assertLessEqual(50, 10, 'first value is not lesstEqual than second')


if __name__ == "__main__":
    unittest.main()

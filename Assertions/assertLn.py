""" assertLn : assertLn method verifies whether the first element is present in the send element, if the first
element is present in second element then the test a passed otherwise test failed.

These two methods will be helpfully when you want to verify presence of a value in a list, tuple, set, and dictionary
"""

import unittest


class Test(unittest.TestCase):
    def testName(self):
        List = ("python", "selenium", "java")
        self.assertIn("python", List, "The item is not available in the list")  # True

    def testName2(self):
        List = ("python", "selenium", "java")
        self.assertIn("pytho", List, 'The item is not available in the list')  # False


if __name__ == "__main__":
    unittest.main()

import unittest
from utest1 import TestCase
from utest2 import verify
from uTest3 import validate


class MyTestCase(unittest.TestCase):

    def suite(self):
        suite = unittest.TestSuite
        # Get all tests from TestClass1 and TestClass2
        tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCase)
        tc2 = unittest.TestLoader().loadTestsFromTestCase(verify)
        tc3 = unittest.TestLoader().loadTestsFromTestCase(validate)

        # Create a test suite combining TestClass1 and TestClass
        smokeTest = unittest.TestSuite([tc1, tc2, tc3])
        unittest.TextTestRunner(verbosity=2).run(smokeTest)
        return suite


if __name__ == '__main__':
    unittest.main()

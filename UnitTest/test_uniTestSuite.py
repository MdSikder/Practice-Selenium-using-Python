import unittest

from UnitTest.utest1 import LogIn
from UnitTest.utest2 import ForgotPass


class MyTestCase(unittest.TestCase):
    def suite(self):
        suite = unittest.TestSuite
        # Get all tests from TestClass1 and TestClass2
        tc1 = unittest.TestLoader().loadTestsFromTestCase(LogIn)
        tc2 = unittest.TestLoader().loadTestsFromTestCase(ForgotPass)

        # Create a test suite combining TestClass1 and TestClass
        smokeTest = unittest.TestSuite([tc1, tc2])
        unittest.TextTestRunner(verbosity=2).run(smokeTest)
        return suite


if __name__ == '__main__':
    unittest.main()

from unittest import TestLoader, TestSuite, TextTestRunner

from StructureComplete.Test.TestCases.TC0001 import Test1
from StructureComplete.Test.TestCases.TC0002 import Test2
from StructureComplete.Test.TestCases.TC0003 import Test3

import testtools as testtools

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Test1),
        loader.loadTestsFromTestCase(Test2),
        loader.loadTestsFromTestCase(Test3)
    ))

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())

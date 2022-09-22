import unittest

from selenium.webdriver.chrome import webdriver
from self import self

from Webdriver_CrossBrowser import driver


class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        print("I will run once before every testdemo")

    def test_methodA(self):
        driver.get("https://www.youtube.com/")
        print("Running method A")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after all tests")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)


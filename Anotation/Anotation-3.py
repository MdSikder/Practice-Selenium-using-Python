import unittest

from selenium.webdriver.chrome import webdriver

from Webdriver_CrossBrowser import driver


class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        print("start" * 30)

    def setUp(self):
        driver.get("https://www.youtube.com/")
        print("I will run once before every testdemo")

    def tearDown(self):
        print("I will run after every testdemo")

    @classmethod
    def tearDownClass(cls):
        driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)

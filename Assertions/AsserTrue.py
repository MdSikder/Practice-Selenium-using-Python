# assertionTrue & false
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testTitle1(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertTrue(titleOfWebPage == "Google")  # True

    def testTitle2(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertTrue(titleOfWebPage == "Google123")  # False


if __name__ == "__main__":
    unittest.main()

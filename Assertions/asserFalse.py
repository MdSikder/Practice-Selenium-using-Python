# assertionFalse
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testTitle1(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertFalse(titleOfWebPage == "Google")  # False

    def testTitle2(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertFalse(titleOfWebPage == "Google123")  # True
        

if __name__ == "__main__":
    unittest.main()


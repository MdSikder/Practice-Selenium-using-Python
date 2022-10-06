import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testTitle1(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertEqual("Google", titleOfWebPage, "Webpage Title is not same ")  # True

    def testTitle2(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertEqual("Google123", titleOfWebPage, "Webpage Title is not same ")  # False


if __name__ == "__main__":
    unittest.main()

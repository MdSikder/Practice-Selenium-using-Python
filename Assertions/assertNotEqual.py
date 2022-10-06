import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testTitle1(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertNotEqual("Google", titleOfWebPage, "Webpage Titles are not same ")  # False

    def testTitle2(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

        titleOfWebPage = driver.title

        self.assertNotEqual("Google123", titleOfWebPage, "Webpage Titles are same ")  # True


if __name__ == "__main__":
    unittest.main()

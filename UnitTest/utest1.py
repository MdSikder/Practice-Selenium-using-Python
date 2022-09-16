import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
        driver = self.driver
        self.driver.maximize_window()
        driver.get(pageUrl)

        driver.find_element(By.XPATH,
                            "//body[1]/header[1]/div[1]/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
            'test')
        time.sleep(5)
        driver.close()


if __name__ == '__main__':
    unittest.main()

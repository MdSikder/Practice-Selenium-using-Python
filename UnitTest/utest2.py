import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver


class verify(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test2(self):
        pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
        driver: WebDriver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        driver.find_element(By.XPATH, "//a[contains(text(),'Selenium Popular Posts')]").click()
        time.sleep(10)
        driver.close()


    def tearDown(self):
        self.driver.quit()

    # This line sets the variable “__name__” to have a value “__main__”.
    # If this file is being imported from another module then “__name__” will be set to the other module's name.
    if __name__ == "__main__":
        unittest.main()

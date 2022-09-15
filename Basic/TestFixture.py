import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class InputFormsCheck(unittest.TestCase):

    # Opening browser
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Testing Single Input Field.
    def test1(self):
        pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        driver.find_element(By.XPATH,
                            "//body[1]/header[1]/div[1]/div[1]/div[1]/section[1]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
            'test')
        time.sleep(5)
        driver.close()

    def test2(self):
        pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
        driver: WebDriver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        driver.find_element(By.XPATH, "//a[contains(text(),'Selenium Popular Posts')]").click()
        time.sleep(10)
        driver.close()

    def test3(self):
        url = "https://www.hhs.gov/coronavirus/community-based-testing-sites/index.html"
        driver: WebDriver = self.driver
        driver.maximize_window()
        driver.get(url)

        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]").click()
        time.sleep(10)
        driver.close()

    # Closing the browser
    def tearDown(self):
        self.driver.quit()


# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()

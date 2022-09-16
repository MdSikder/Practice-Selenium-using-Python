import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver


class validate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

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

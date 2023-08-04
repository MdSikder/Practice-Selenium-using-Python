import time
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


path = 'C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver\\chromedriver.exe'
class main(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        pageUrl = "https://www.google.com/"
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(pageUrl)
        wait = WebDriverWait(driver, 10)
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(
            "admin@klovercloud.com")
        time.sleep(2)


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()




import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def setUp(self):
    self.driver = webdriver.Chrome()


def test1(self):
    pageUrl = "https://www.yatra.com"
    driver = self.driver
    self.driver.maximize_window()
    self.driver.get(pageUrl)
    #wait = WebDriverWait(driver, 10)
    time.sleep(2)

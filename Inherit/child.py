import time

from selenium.webdriver.common.by import By

from Inherit.base import main

from selenium.webdriver.support.wait import WebDriverWait


def test1(self):
    pageUrl = "https://www.google.com/"
    driver = self.driver
    self.driver.maximize_window()
    self.driver.get(pageUrl)
    wait = WebDriverWait(driver, 10)
    time.sleep(2)
    driver.find_element(By.XPATH, "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(
        "admin@klovercloud.com")

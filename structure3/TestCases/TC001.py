import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from structure3.PageObject.POMTC001 import Home
from structure3.PageObject.Locators import Locator
from structure3.Base.EnvironmentSetup import EnvironmentSetup


class Test1(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://www.google.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        home = Home(driver)
        home.search_text.send_keys('LambdaTest', Keys.ENTER)

        # driver.find_element(By.XPATH, Locator.search_text).send_keys('kabir', Keys.ENTER)
        time.sleep(10)

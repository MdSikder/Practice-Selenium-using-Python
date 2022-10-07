import time

from selenium.webdriver.common.by import By

from structure3.PageObject.POMTC002 import Main

from structure3.PageObject.Locators import Locator
from structure3.Base.EnvironmentSetup import EnvironmentSetup
from structure3.screenShots.screenShots import SS

ss_path = "/TC002/"


class Test1(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        main = Main(driver)

        main.User_Name.send_keys('mayabi')
        time.sleep(3)

        main.Visit_Us.click()
        time.sleep(2)
        ss = SS(driver)
        ss.ScreenShot(ss_path + "UserName")

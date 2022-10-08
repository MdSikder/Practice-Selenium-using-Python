import time

from selenium.webdriver.common.by import By

from structure3.PageObject.POMTC002 import Main
from StructureComplete.POM.Pages.POMTC0002 import Main
from StructureComplete.Test.TestUtility.screenShot import SS
from StructureComplete.Base.EnvironmentSetup import EnvironmentSetup

ss_path = "/TC0002/"


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

        file_name = ss_path + "scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

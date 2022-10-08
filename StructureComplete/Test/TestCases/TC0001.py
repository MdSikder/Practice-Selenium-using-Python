import time

from selenium.webdriver import Keys

from StructureComplete.POM.Pages.POMTC0001 import Home
from StructureComplete.Test.TestUtility.screenShot import SS
from StructureComplete.Base.EnvironmentSetup import EnvironmentSetup

ss_path = "/TC0001/"


class Test1(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://www.google.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        home = Home(driver)
        home.search_text.send_keys('Test-1-Check', Keys.ENTER)

        # driver.find_element(By.XPATH, Locator.search_text).send_keys('kabir', Keys.ENTER)
        time.sleep(10)
        ss = SS(driver)

        file_name = ss_path + "Test-1_scrrenshot_" + time.asctime().replace(":", "_") + ".png"

        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)


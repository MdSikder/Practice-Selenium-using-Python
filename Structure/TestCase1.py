import time

from selenium.webdriver import Keys

from Structure.Base import EnvironmentSetup
from Practice_Selenium_Using_Python.Structure.Base import EnvironmentSetup
from Practice_Selenium_Using_Python.Structure.PageObjectModel import Locator

from selenium.webdriver.common.by import By
from Structure.screenShot import SS

Loc = Locator()
screen_shot = ("C:\\Users\\User\\PycharmProjects\\pythonProject\\LearningSeleniumWithPython"
               "\\screenShot\\ScreenShots\\home2.png")
# ss_path = "//ssFiles//" **also worked**
ss_path = "/ssFiles/"  # **prefer**


class Home(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://www.google.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        ss = SS(driver)

        driver.find_element(By.XPATH, Loc.text).send_keys('kabir', Keys.ENTER)
        time.sleep(3)
        # driver.get_screenshot_as_file(screen_shot)
        ss.ScreenShot(ss_path + "home1.png")

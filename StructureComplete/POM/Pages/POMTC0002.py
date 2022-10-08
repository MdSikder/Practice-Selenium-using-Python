from selenium.webdriver.common.by import By
from StructureComplete.POM.AllLocators.Locators import Locator


class Main(object):
    def __init__(self, driver):
        self.driver = driver

        self.User_Name = driver.find_element(By.XPATH, Locator.User_Name)
        self.Visit_Us = driver.find_element(By.XPATH, Locator.Visit_Us)

    def User_Name(self):
        return self.User_Name

    def getVisit_Us(self):
        return self.User_Name

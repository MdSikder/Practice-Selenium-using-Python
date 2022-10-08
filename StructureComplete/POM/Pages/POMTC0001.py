from selenium.webdriver.common.by import By
from StructureComplete.POM.AllLocators.Locators import Locator


class Home(object):
    def __init__(self, driver):
        self.driver = driver

        self.search_text = driver.find_element(By.XPATH, Locator.search_text)

    def getSearchText(self):
        return self.search_text

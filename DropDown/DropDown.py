import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        pageUrl = "https://www.orangehrm.com/orangehrm-30-day-trial/"
        driver = self.driver
        self.driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(pageUrl)
        time.sleep(2)

        # scroll
        driver.execute_script("window.scrollBy(0,600)", "")
        time.sleep(2)

        """PATH"""

        UserName = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_subdomain']")
        name = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_Name']")
        email = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_Email']")
        PhoneNumber = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_Contact']")

        """ Actions """
        UserName.send_keys("porag")
        name.send_keys("sikder")
        email.send_keys("test@gmail.com")
        PhoneNumber.send_keys("01677854972")

        """ DropDown Method"""

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        pageUrl = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt"
        driver = self.driver
        self.driver.maximize_window()
        driver.get(pageUrl)
        driver.implicitly_wait(10)

        driver.switch_to.frame("iframeResult")

        # Alert : Accept
        alert_button1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
        alert_button1.click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        print("Popup Accept Successful")

        '''Alert : Dismiss'''
        alert_button_2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
        alert_button_2.click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.dismiss()
        print("Popup Dismiss Successful")



        #Alert: Send Values
        alert_button_3 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
        alert_button_3.click()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Md Kuddus")
        alert.accept()
        time.sleep(5)
        print("Popup Value Sending Successful")
        driver.close()


if __name__ == '__main__':
    unittest.main()

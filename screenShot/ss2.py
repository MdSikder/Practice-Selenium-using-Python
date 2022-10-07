import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def testTitle1(self):
        driver = webdriver.Chrome()
        driver.get("https://letskodeit.teachable.com/")
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        time.sleep(2)
        driver.find_element(By.NAME, "commit").click()
        time.sleep(5)
        destinationFileName = ""

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")


if __name__ == "__main__":
    unittest.main()

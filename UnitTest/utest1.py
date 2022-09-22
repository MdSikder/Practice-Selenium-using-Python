import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.maximize_window()
        driver.get(pageUrl)
        time.sleep(2)

        driver.find_element(By.ID, "inputUsername").send_keys('porag')
        print("Username Input Successfully")
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/input[2]").send_keys(
            'rahulshettyacademy')
        print("Password Input Successfully")
        time.sleep(2)

        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div["
                                      "1]/span[1]/input[1]").click()
        print("Select Remember my username")
        time.sleep(2)

        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div["
                                      "1]/span[2]/input[1]").click()
        print("Select Agree Button")
        time.sleep(2)

        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
        print("You are successfully logged in")
        time.sleep(4)

        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        print("You are successfully logged Out")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
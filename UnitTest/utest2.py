import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver


class ForgotPass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test2(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver: WebDriver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        time.sleep(2)

        # Forgot your password
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/a[1]").click()
        time.sleep(2)
        print("Click On Forgot password")

        # input name
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]").send_keys(
            'Porag')
        print("input name")
        time.sleep(2)

        # input email
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[2]").send_keys(
            'test@gmail.com')
        print("input Email")
        time.sleep(2)

        # input phone number
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[3]").send_keys(
            "017155578566")
        print("input phone number")
        time.sleep(2)

        # Click to reset password
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[2]").click()
        print("Click to reset password")
        time.sleep(2)

        # input phone number
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[2]").click()
        print("Click to reset password")
        time.sleep(2)

        # go to login page
        driver.find_element(By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
        print("Click go to login page")
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

    # This line sets the variable “__name__” to have a value “__main__”.
    # If this file is being imported from another module then “__name__” will be set to the other module's name.
    if __name__ == "__main__":
        unittest.main()

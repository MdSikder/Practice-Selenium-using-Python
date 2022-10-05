import time

from selenium.webdriver.common.by import By

from structure3.PageObject.POMTC002 import Main

from structure3.PageObject.Locators import Locator
from RahulShettyAcademy.Base.EnvironmentSetup import EnvironmentSetup
from RahulShettyAcademy.PageObjectModel.PomLogIn import Main
from RahulShettyAcademy.PageObjectModel.PomForgotPassword import ForgotPass


class Test1(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        main = Main(driver)

        main.UserNameBar.send_keys('porag')
        time.sleep(2)
        main.PasswordBar.send_keys('123!@')
        time.sleep(2)
        main.SingInButton.click()
        time.sleep(2)

        main.ForgotYourPassword.click()
        self.driver.implicitly_wait(5)
        time.sleep(4)

        forgotPass = ForgotPass(driver)

        forgotPass.NameBar.send_keys('porag')
        time.sleep(2)
        forgotPass.EmailBar.send_keys('test@gmail.com')
        time.sleep(2)
        forgotPass.PhoneNumberBar.send_keys('01257894163')
        time.sleep(3)
        forgotPass.ResetButton.click()
        time.sleep(2)
        # forgotPass.PickPass.get_Text()

        forgotPass.GoToLoginButton.click()
        self.driver.implicitly_wait(5)
        time.sleep(3)

        main.UserNameBar.send_keys("Porag")
        time.sleep(1)

        main.PasswordBar.send_keys("rahulshettyacademy")
        time.sleep(2)

        main.SingInButton.click()
        self.driver.implicitly_wait(5)
        time.sleep(5)


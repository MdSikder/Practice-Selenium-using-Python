import time
from telnetlib import EC

import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from Src.Locators.locators import Locator

from Src.Page_object_model.pom_loginPage import LogInPage
from Src.screen_shots.screen_shots import SS
from Src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ss_path = "/Applications/PHP/"


class TestCreatePHP(EnvironmentSetup):
    def test_Laravel_default_01(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! URL found ')

        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # ******************************Login**********************************
        print("----------------------Cluster LogIn-----------------------------------")
        # page object
        log = LogInPage(driver)  # LogIn page

        # input email
        try:
            if log.Email_box.is_enabled():
                print("Email box is enabled")
                log.Email_box.send_keys('admin@klovercloud.com')
                time.sleep(1)
            else:
                print("Email box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        else:
            print('Successfully inputted email')

        # input pass
        try:
            if log.Password_box.is_enabled():
                print("Password box is enabled")
                log.Password_box.send_keys('Hello@1234')
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully inputted Password')

        # To show password
        try:
            if log.Toggle_Visibility_Button.is_enabled():
                print("Toggle Visibility Button box is enabled")
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully showed & hided Password')

        # Click On SignIn button
        try:
            if log.Sign_In_button.is_enabled():
                print("Sign In button is clickable")
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(7)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully logged in')

        print("****************** Create PHP Laravel Application based on Team: default *********************")

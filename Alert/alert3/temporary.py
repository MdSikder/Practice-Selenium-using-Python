import pickle
import time

import simple_colors
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.Locators.locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from urllib.request import urlopen
from urllib.error import *

from src.base.environment_setup import EnvironmentSetup

ss_path = "/LogIn"


class TestDeploy(EnvironmentSetup):

    def test_cluster_login(self):
        driver = self.driver
        pageUrl = "https://eks.alpha.klovercloud.io/"
        username = "admin@klovercloud.com"
        password = "Hello@124"
        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print(Fore.LIGHTRED_EX + "HTTP error", e)

        except URLError as e:
            print(Fore.LIGHTRED_EX + "Opps ! Page not found!", e)

        else:
            print(Fore.YELLOW + 'Yeah ! URL found ')

        driver.get(pageUrl)
        driver.implicitly_wait(20)
        time.sleep(2)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Email_box)))
            print("Email_box is inputable")
            Email_box.send_keys(username)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put email in Email_box')

        # put password
        try:
            Password_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Password_box)))
            print("Password_box is inputable")
            Password_box.send_keys(password)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put password in Password_box')

        # click on Toggle_Visibility_Button
        try:
            Toggle_Visibility_Button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Toggle_Visibility_Button)))
            print("Toggle_Visibility_Button is clickable")
            Toggle_Visibility_Button.click()
            time.sleep(1)
            Toggle_Visibility_Button.click()
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')
        # Click on Sign In button

        try:
            Sign_In_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Sign_In_button)))
            print("Password_box is inputable")
            Sign_In_button.click()
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.alert_is_present)
            time.sleep(1)
            alert = driver.switch_to.alert
            text = alert.text
            time.sleep(1)
            print(text)
            pass

            # if "some Text" in text:
            #     print("Booking successful")
            # elif "some other text" in text:
            #     print("booking not successful")
            self.driver.implicitly_wait(3)
            # time.sleep(2)

            # try:
            #     WebDriverWait(driver, 10).until(EC.alert_is_present)
            #     alert = driver.switch_to.alert
            #     text = alert.text
            #     if "some Text" in text:
            #         print("Booking successful")
            #     elif "some other text" in text:
            #         print("booking not successful")
            # except:
            #     print("no alert")

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully click on Sign In button')

        time.sleep(10)

        # # check error message have or not
        # try:
        #     LogIn_Authentication_Error = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
        #     if LogIn_Authentication_Error.is_displayed():
        #         print("\n")
        #         print('Shown a error message: ',
        #               simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
        #         print("\n")
        #         self.driver.close()
        #         self.driver.stop()
        #         # return FileExistsError
        #     else:
        #         pass
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)

    # def test_cookies(self):
    #     driver = self.driver
    #     pageUrl = "https://console.klovercloud.com/auth/login"
    #     username = "admin@klovercloud.com"
    #     password = "Hello@1234"
    #     driver.get(pageUrl)
    #     driver.implicitly_wait(20)
    #     time.sleep(2)
    #     cookies = pickle.load(open("cookies.pkl", "rb"))
    #     print("\n", cookies, "\n")
    #     for cookie in cookies:
    #         driver.add_cookie(cookie)

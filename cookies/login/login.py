import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):  # Checks if the instance expiry a float
            cookie['expiry'] = int(cookie['expiry'])  # it converts expiry cookie to a int
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):
    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()


# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "C:/Users/User/PycharmProjects/Practice_Selenium_Using_Python/cookies/login/cookies.txt"

# Initial load of the domain that we want to save cookies for
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.get("https://www.google.com")
# chrome.get("https://www.hackerrank.com/login")
#
# chrome.find_element(By.XPATH,
#                     "//body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
#     "infunig1986")
# chrome.find_element(By.XPATH,
#                     "//body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys(
#     "TestUserAccount")
# chrome.find_element(By.XPATH,
#                     "//body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]/div[1]/span[1]").click()
# # chrome.find_element(By.XPATH, "(//button[@name='commit'])[2]").click()
# save_cookies(chrome, cookies_location)
# chrome.close()

# Load of the page you can't access without cookies, this one will fail
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.get("https://www.hackerrank.com/settings/profile")
# chrome.close()

# Load of the page you cant access without cookies, this one will go through
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
load_cookies(chrome, cookies_location)
chrome.get("https://www.hackerrank.com/settings/profile")
time.sleep(5)


# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.get("https://google.com")
# time.sleep(2)
# pprint.pprint(chrome.get_cookies())
# print("=========================\n")
#
# delete_cookies(chrome, domains=["www.google.com"])
# pprint.pprint(chrome.get_cookies())
# print("=========================\n")
#
# delete_cookies(chrome)
# pprint.pprint(chrome.get_cookies())

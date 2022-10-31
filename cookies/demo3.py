import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from cookies.login.login import save_cookies
cookies_location = "C:/Users/User/PycharmProjects/Practice_Selenium_Using_Python/cookies/login/cookies2.txt"
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.get("https://www.google.com")
chrome.get("https://www.hackerrank.com/login")

chrome.find_element(By.XPATH,
                    "//body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
    "infunig1986")
chrome.find_element(By.XPATH,
                    "//body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys(
    "TestUserAccount")
chrome.find_element(By.XPATH,
                    "//body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]/div[1]/span[1]").click()
# chrome.find_element(By.XPATH, "(//button[@name='commit'])[2]").click()
save_cookies(chrome, cookies_location)
chrome.close()
chrome.quit()

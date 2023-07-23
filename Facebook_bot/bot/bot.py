import time
from telnetlib import EC

# import self as self
from selenium import webdriver
# from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import XLutils
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument(
    'user-data-dir=C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromeprofile')
chrome_driver = "C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
path = "C:\\Users\\KloverCloud\\PycharmProjects\\Practice_Selenium_Using_Python\\Facebook_bot\\excel\\hello.xlsx"
url = "https://www.facebook.com/groups/353266859276449/members"

driver.get("https://www.facebook.com/groups/353266859276449/members")  # Click on the "Members" tab
time.sleep(5)
members_tab = driver.find_element_by_link_text('People')
members_tab.click()
time.sleep(5)

rows = XLutils.getRowCount(path, "Sheet1")
print("Number of Rows i a Excel: ", rows)
lst_status = []
for r in range(2, rows + 1):
    useremail = XLutils.readData(path, 'Sheet1', r, 1)
    password = XLutils.readData(path, 'Sheet1', r, 2)
    exp = XLutils.readData(path, 'Sheet1', r, 3)

    search = driver.find_element_by_xpath(
        "//*[@id='mount_0_0_bu']/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/span/span/div/label/input")
    search.send_keys(useremail)
    time.sleep(3)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    user = driver.find_element_by_xpath("//a[contains(text(),'" + useremail + "')]")
    user.click()
    time.sleep(7)

    # for mouse hover
    # actions.move_to_element(user).perform()
    # time.sleep(3)

    messenger = driver.find_element_by_xpath(
        "//*[@id='mount_0_0_0n']/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div/div[1]/div[2]/span/span")
    messenger.click()
    time.sleep(2)

    actions.send_keys('message')
    time.sleep(3)
    actions.send_keys(Keys.ENTER)
    time.sleep(5)

    selectfrom_Computer = driver.find_element_by_xpath("")
    driver.find_element(By.XPATH, selectfrom_Computer).click()
    time.sleep(5)

    UploadFilePath = "C:\\Users\\KloverCloud\\Desktop\\files\\qw.jpg"
    pyautogui.typewrite(UploadFilePath)
    time.sleep(2)

    pyautogui.press('enter')
    time.sleep(3)

    try:
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
    except:
        print("no cookies Alert")

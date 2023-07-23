
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
import openpyxl
from openpyxl import load_workbook
import XLutils
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromedriver.exe")
# driver.get("http://newtours.demoaut.com/")
# driver.maximize_window()

path = "C:\\Users\\KloverCloud\\PycharmProjects\\Practice_Selenium_Using_Python\\Facebook_bot\\excel\\hello.xlsx"
path2 = "C:\\Users\\KloverCloud\\PycharmProjects\\Practice_Selenium_Using_Python\\Facebook_bot\\test.xlsx"
# rows = XLutils.getRowCount(path, "Sheet1")

driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
driver.maximize_window()
time.sleep(5)

actions = ActionChains(driver)
# actions.send_keys(Keys.ENTER)
# actions.perform()

element_to_hover_over = driver.find_elements_by_xpath("//*[@id='free-trial-link-anchor']")
# element_to_hover_over
time.sleep(2)
# hover = ActionChains(driver).move_to_element(element_to_hover_over)
# hover.perform()
# time.sleep(5)

# actions = ActionChains(driver)
# actions.move_to_element(element_to_hover_over).build().perform()

time.sleep(5)

driver.close()





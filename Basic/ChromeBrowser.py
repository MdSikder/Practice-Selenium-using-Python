
import time

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service


driver = webdriver.Chrome()
#driver = webdriver.Chrome(r'C:\chrome\chromedriver.exe')

url = "http://www.facebook.com/"

driver.get(url)
driver.maximize_window()

time.sleep(5)
driver.quit()




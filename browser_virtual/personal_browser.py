from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("user-data-dir=C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver\\chromeprofile")
chrome_driver = "C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)  # driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(3)
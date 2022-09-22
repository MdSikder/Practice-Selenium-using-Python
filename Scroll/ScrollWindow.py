import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,2000)", "")

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()

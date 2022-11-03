from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

st1 = time.time()
driver.get("https://testautomationpractice.blogspot.com/")
Click_me = "//body[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/aside[1]/div[" \
           "1]/div[2]/div[1]/button[1] "
driver.find_element(By.XPATH, Click_me).click()
time.sleep(5)
# driver.switch_to_alert().accept()  # close alert window using "OK" button
# create alert object
alert = Alert(driver)
time.sleep(2)

# get alert text
print(alert.text)

# accept the alert
alert.accept()

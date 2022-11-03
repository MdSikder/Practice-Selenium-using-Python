from attr import s
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# get ide.geeksforgeeks.org
driver.get("https://ide.geeksforgeeks.org/tryit.php/WXYeMD9tD4")

# create alert object
alert = Alert(driver)
time.sleep(2)

driver.switch_to_window(s.pop())

driver.switch_to.alert

switch_to.alert
switch_to.By()


# get alert text
print(alert.text)

# accept the alert
alert.accept()

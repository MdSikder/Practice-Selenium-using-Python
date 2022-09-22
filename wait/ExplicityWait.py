import time

import ec as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
print(driver.title)

wait = WebDriverWait(driver, 10)

element = wait.until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Mobiles')]")))

# element = wait.until(ec.element_to_be)
element.click()
time.sleep(2)
driver.close()

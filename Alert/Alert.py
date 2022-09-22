import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from self import self

from Webdriver_CrossBrowser import driver

self.driver = webdriver.Chrome()
driver.implecity_wait(10)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame("iframeResult")

# Alert : Accept
alert_button_1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]")
alert_button_1.click()
time.sleep(5)

from telnetlib import EC

import self
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Webdriver_CrossBrowser import driver

ApplicationName = "102"

driver.find_element(By.XPATH, "//span[contains(text()," + ApplicationName + ")]")
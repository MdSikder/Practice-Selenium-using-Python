"""  Conditional Command

1. is_selected()
2.is_enabled()
3. is_displayed()  """
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.LINK_TEXT, "Courses")
time.sleep(5)

# print value
print(element.is_displayed())
driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/button[1]"))
)
time.sleep(3)
driver.close()

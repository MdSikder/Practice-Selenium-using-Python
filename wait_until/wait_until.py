import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://eks.rakibefstestmaincluster782.klovercloud.io/")
element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//body[1]/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]")))
element.click()
time.sleep(5)

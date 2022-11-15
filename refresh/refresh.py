from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
st1 = time.time()
driver.get("https://www.google.com/")
driver.implicitly_wait(20)
time.sleep(2)
# driver.refresh()

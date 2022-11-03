from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

Email_box = "//input[@id='mat-input-0']"  # xpath
Email_box_test = "//input[@id='mat-inpu-0']"  # xpath
Password_box = "//input[@id='mat-input-1']"  # xpath
Toggle_Visibility_Button = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                           "4]/button "  # xpath
Sign_In_button = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

st1 = time.time()
driver.get("https://eks.rakibefstestmaincluster782.klovercloud.io/")
driver.maximize_window()

driver.find_element(By.XPATH, Email_box).send_keys(10)
time.sleep(1)
driver.find_element(By.XPATH, Password_box).send_keys(10)
time.sleep(1)
driver.find_element(By.XPATH, Toggle_Visibility_Button).click()
time.sleep(1)
driver.find_element(By.XPATH, Toggle_Visibility_Button).click()
time.sleep(1)
driver.find_element(By.XPATH, Sign_In_button).click()
time.sleep(5)
# driver.switch_to_alert().accept()  # close alert window using "OK" button
# create alert object
alert = Alert(driver)
time.sleep(2)

# get alert text
print(alert.text)

# accept the alert
# alert.accept()
driver.close()

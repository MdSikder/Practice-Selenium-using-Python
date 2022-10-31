import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from cookies.login.login import save_cookies

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://eks.rakibefstestmaincluster782.klovercloud.io/")
driver.maximize_window()

# input email
driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("admin@klovercloud.com")
time.sleep(2)

# input password
driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("Hello@1234")
time.sleep(2)

# click eye button to check password
driver.find_element(By.XPATH,
                    "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/div[1]/mat-form-field[2]/div["
                    "1]/div[1]/div[4]/button[1]/span[1]/mat-icon[1]/*[1]").click()
time.sleep(2)

# again click on eye button to hide password
driver.find_element(By.XPATH,
                    "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/div[1]/mat-form-field[2]/div["
                    "1]/div[1]/div[ "
                    "4]/button[1]/span[1]/mat-icon[1]/*[1]").click()
time.sleep(2)

# click on SignUp
driver.find_element(
    By.XPATH, "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]").click()
driver.implicitly_wait(10)
time.sleep(7)
print("LogIn successfully ")

print("Welcome to dashboard")

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies has been created
print(cookies)  # print all the cookie pairs
cookies_location = "C:/Users/User/PycharmProjects/Practice_Selenium_Using_Python/cookies/login/cookies.txt"
driver.save_cookies
save_cookies(driver, cookies_location)
driver.close()

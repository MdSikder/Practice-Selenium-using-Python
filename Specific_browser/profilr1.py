import time

from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

options = Options()
options.add_argument('--profile-directory=Profile 1')

# options.add_argument("user-data-dir=C:\\Users\\KloverCloud\\AppData\\Local\\Google\\Chrome\\User Data")


options.add_argument("--user-data-dir=C:/Users/KloverCloud/AppData/Local/Google/Chrome/User Data")
browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
driver = uc.Chrome(executable_path=browser_path, options=options)

driver.maximize_window()
driver.get('https://www.facebook.com/')
driver.get("https://mail.google.com/mail/u/0/#inbox")
time.sleep(5)
driver.close()

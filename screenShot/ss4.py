import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def capture_screenshot(d, path):
    file_name = path + "scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    d.save_screenshot(file_name)


driver = webdriver.Chrome()
driver.get("https://google.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.save_screenshot("./ScreenShot/error.jpg")
elem = driver.find_element(By.XPATH, "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
elem.send_keys('10')
time.sleep(2)
capture_screenshot(driver, "./ScreenShots/")

driver.quit()

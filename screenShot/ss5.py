import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.save_screenshot("./ScreenShot/error.jpg")
elem = driver.find_element(By.XPATH, "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
elem.send_keys('10')
time.sleep(2)
# driver.get_screenshot_as_file("C:\\Users\\User\\Desktop\\New folder\\home.png")
driver.get_screenshot_as_file("C:\\Users\\User\\PycharmProjects\\pythonProject\\LearningSeleniumWithPython\\screenShot"
                              "\\ScreenShots\\home.png")

driver.quit()

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

driver.save_screenshot("./ScreenShot/error.jpg")

driver.switch_to.frame("iframeResult")
driver.execute_script("myFunction()")

elem = driver.find_element(By.ID, "mySubmit")
elem.screenshot("./ScreenShot/ele.jpg")

driver.execute_script("argument[0].style.border='3px solid red'", elem)
driver.switch_to.default_content()

frames = driver.find_element(By.TAG_NAME, "iframe")
for frame in frames:
    print(frame.get_attribute("id"))
print(len(frames))


capture_screenshot(driver, "./ScreenShots/")

from selenium import webdriver
from selenium.webdriver.common.by import By

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

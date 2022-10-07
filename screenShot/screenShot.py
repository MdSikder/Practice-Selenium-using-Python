from selenium import webdriver
from selenium.webdriver.common.by import By


class ScreenShots():
    def testTitle1(self):
        driver = webdriver.Chrome()
        driver.get("https://google.com/")

    def test1(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.find_element(By.LINK_TEXT, "Login").click()



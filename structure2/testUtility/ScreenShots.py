

from selenium import webdriver


class SS:

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = "C:\\Users\\User\\PycharmProjects\\pythonProject\\LearningSeleniumWithPython\\structure2\\testUtility\\ScreenShots"
        self.driver.get_screenshot_as_file(directory + path)

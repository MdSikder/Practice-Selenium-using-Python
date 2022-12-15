# import time
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.common.by import By
# from self import self
# from Webdriver_CrossBrowser import driver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.w3schools.com/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//*[@id='search2']").send_keys("test")
# time.sleep(4)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.w3schools.com/"
driver.get(url)


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    diis = element._parent

    def apply_style(s):
        diis.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                            element, s)

    original_style = element.get_attribute('style')
    apply_style("border: 2px solid yellow;")
    time.sleep(.3)
    apply_style(original_style)


# open_window_elem = driver.find_element(By.ID, "openwindow")
kupa = driver.find_element(By.XPATH, "//*[@id='search2']")
highlight(kupa)
kupa.send_keys("kupa")
time.sleep(4)

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


def highlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)

    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)


# open_window_elem = driver.find_element_by_id("openwindow")
# highlight(open_window_elem, 3, "blue", 5)

kupa = driver.find_element(By.XPATH, "//*[@id='search2']")
highlight(kupa, 3, "yellow", 3)
kupa.send_keys("kupa")
time.sleep(4)
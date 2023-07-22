import pickle
import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test1():
    # pytest.skip("Skipping test...later I will implement...")
    username = "admin@klovercloud.com"
    password = "Hello@1234"
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument('user-data-dir=C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromeprofile')
    chrome_driver = "C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)  # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/groups/261000217971523")

    time.sleep(5)

    try:
        # Click on the "People" link in the left sidebar
        people_link = driver.find_element_by_xpath("//a[contains(@href,'/browse/group_members/')]")
        people_link.click()
        time.sleep(5)

        # Mouse hover on the first member and click on "Messenger"
        first_member = driver.find_element_by_xpath("(//div[@role='grid'])[2]/div[1]/div[1]")
        ActionChains(driver).move_to_element(first_member).perform()
        time.sleep(2)
        messenger_button = driver.find_element_by_xpath("(//div[@aria-label='Send Message'])[1]")
        messenger_button.click()
        time.sleep(2)

        # Write a message and send it
        message = "Hello member's name"
        text_input = driver.find_element_by_xpath("//div[@role='textbox']")
        text_input.send_keys(message)
        text_input.send_keys(u'\ue007')  # Press Enter key

        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
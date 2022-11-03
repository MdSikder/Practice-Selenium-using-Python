import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import time
from telnetlib import EC

import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from Src.Locators.locators import Locator

from Src.Page_object_model.pom_loginPage import LogInPage
from Src.screen_shots.screen_shots import SS
from Src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from attr import s
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demoqa.com/")

    def test_Click(self):

        signup =  driver.f (By.LINK_TEXT, 'Registration').click()

    def test_Form(self):
        self.First_name = self.driver.find_element_by_xpath("//*[@id='name_3_firstname']").send_keys("Santosh")
        self.Last_name = self.driver.find_element_by_xpath("//*[@id='name_3_lastname']").send_keys("Kumar")
        self.Status = self.driver.find_element_by_xpath("//*[@id='pie_register']/li[2]/div/div/input[1]").click()
        self.Hobby = self.driver.find_element_by_xpath("//*[@id='pie_register']/li[3]/div/div[1]/input[2]").click()
        """self.Country = self.driver.find_element_by_id("dropdown_7")
        for option in self.Country.find_elements_by_tag_name('option'):
            if option.text == 'India':
                option.click()
                break"""
        self.Country = Select(self.driver.find_element_by_id("dropdown_7"))
        self.Country.select_by_value('India')
        self.month = Select(self.driver.find_element_by_xpath("//*[@id='mm_date_8']"))
        self.month.select_by_index(4)
        self.day = Select(self.driver.find_element_by_xpath("//*[@id='dd_date_8']"))
        self.day.select_by_index(11)
        self.year = Select(self.driver.find_element_by_xpath("//*[@id='yy_date_8']"))
        self.year.select_by_value('2014')
        self.phone = self.driver.find_element_by_xpath("//*[@id='phone_9']").send_keys("9738993098")
        self.username = self.driver.find_element_by_xpath("//*[@id='username']").send_keys("santu_tz6")
        self.email = self.driver.find_element_by_xpath("//*[@id='email_1']").send_keys("santu6@gmail.com")
        self.about = self.driver.find_element_by_xpath("//*[@id='description']").send_keys(
            "Very much interested in Testing")
        self.password = self.driver.find_element_by_xpath("//*[@id='password_2']").send_keys("Secret97@1")
        self.confirm = self.driver.find_element_by_xpath("//*[@id='confirm_password_password_2']").send_keys(
            "Secret97@1")
        self.submit = self.driver.find_element_by_xpath("//*[@id='pie_register']/li[14]/div/input").click()
        self.success = self.driver.find_element_by_xpath("//*[@id='post-49']/div/p").get_attribute('text')
        time.sleep(3)
        self.expected_text = "Error: Username already exists"
        self.assertEquals(self.success, self.expected_text)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()

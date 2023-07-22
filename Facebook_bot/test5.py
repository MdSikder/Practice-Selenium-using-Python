from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pickle
import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from bs4 import BeautifulSoup



# Start the browser (replace 'chromedriver_path' with the path to your chromedriver executable)
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument(
    'user-data-dir=C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromeprofile')
chrome_driver = "C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)  # driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.facebook.com/groups/261000217971523")

# Start the Selenium WebDriver (Chrome in this example)

# Open the URL
url = 'https://www.facebook.com/groups/353266859276449/members'
driver.get(url)

# Wait for 5 seconds
time.sleep(5)

# Click on the "people" tab
# Click on the "Members" tab
members_tab = driver.find_element_by_link_text('People')
members_tab.click()
time.sleep(5)
# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='grid']")))

# Extract the HTML source
html_source = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML source using BeautifulSoup
soup = BeautifulSoup(html_source, 'html.parser')

# Extract group members
group_members = []
member_elements = soup.find_all('a', attrs={'role': 'link'})
for member_element in member_elements:
    member_name = member_element.text
    if member_name:
        group_members.append(member_name)

# Print the group members
print("Group Members:")
for member in group_members:
    print(member)

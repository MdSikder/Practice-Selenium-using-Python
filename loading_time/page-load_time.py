from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.set_page_load_timeout(15)
while True:
    try:
        browser.get("https://eks.rakibefstestmaincluster782.klovercloud.io/")
        print("URL successfully Accessed")
        # continue with the next steps
    except TimeoutException as e:
        print("Page load Timeout Occurred. Refreshing !!!")
        browser.refresh()

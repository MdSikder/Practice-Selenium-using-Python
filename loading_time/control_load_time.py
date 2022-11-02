from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

st1 = time.time()
browser.get("http://app1.helwan.edu.eg/Commerce/HasasnUpMlist.asp")
browser.maximize_window()
et1 = time.time()
el1 = et1 - st1
print(f"Elapsed Time is: {el1} Seconds")
# 10.48

st2 = time.time()
my_id = browser.find_element("name", "x_st_settingno")
submitting = browser.find_element("name", "Submit")
my_id.send_keys(18760)
submitting.click()
et2 = time.time()
el2 = et2 - st2

link_to_natega = browser.find_element("xpath", '//*[@id="ewlistmain"]/tbody/tr[3]/td[9]/font/b/span/a')
link_to_natega.click()

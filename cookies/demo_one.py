"""operations on cookies

capture all cookies from browser
count number of cookies
read cookie pairs
adding new cookies
deleting specific cookie by using name of cookie
seleting all the cookies"""


from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")

# Capture all the cookies created by browser
cookies = driver.get_cookies()

print(len(cookies))  # print number of cookies has been created
print(cookies)  # print all the cookie pairs

# Adding new cookie to browser
cookie = {'name': 'Mycookie', 'value': '12345678'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()

print(len(cookies))  # print number of cookies after adding new cookie
print(cookies)  # print all the cookie pairs

# deleting cookie
driver.delete_cookie('Mycookie')

cookies = driver.get_cookies()

print(len(cookies))  # print number of cookies after deleting the cookie
print(cookies)  # print all the cookie pairs

# deleting all the cookies
driver.delete_all_cookies()  # delete all cookies
cookies = driver.get_cookies()

print(len(cookies))  # print number of cookies after deleting the cookie
print(cookies)

driver.close()

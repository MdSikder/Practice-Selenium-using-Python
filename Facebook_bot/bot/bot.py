from selenium.webdriver.common.by import By
import XLutils
from selenium import webdriver

path = "C:\\Users\\KloverCloud\\PycharmProjects\\Practice_Selenium_Using_Python\\Facebook_bot\\excel\\hello.xlsx"
rows = XLutils.getRowCount(path, "Sheet1")
print("Number of Rows i a Excel: ", rows)
lst_status = []
for r in range(2, rows + 1):
    useremail = XLutils.readData(path, 'Sheet1', r, 1)
    password = XLutils.readData(path, 'Sheet1', r, 2)
    exp = XLutils.readData(path, 'Sheet1', r, 3)
    print(useremail)
    print(password)


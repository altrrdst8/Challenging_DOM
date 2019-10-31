from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains
import re
from collections import defaultdict

driver = webdriver.Chrome("C:\Program Files (x86)\Python\WebDrivers\chromedriver.exe")
action = ActionChains(driver)
#driver = webdriver.Firefox("C:\Program Files (x86)\Python\WebDrivers\geckodriver.exe")
# driver = webdriver.Firefox()
# driver = webdriver.IE()

# TEST Elements --------------------------------------------------------------------------------------------------------

driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/challenging_dom")
driver.implicitly_wait(4)

tableID = driver.find_element_by_xpath("//div[@id='content']/div/div/div/div[2]/table")
tableHead = tableID.find_elements_by_tag_name('thead')
tableBody = tableID.find_elements_by_tag_name('tbody')

for row in tableBody:
    tableColumn = row.find_elements_by_tag_name('tr')
    rowQty = len(tableColumn)
    rowQty -= 1
    while rowQty >= 0:
        print(tableColumn[rowQty].get_attribute('innerText'))
        rowQty -= 1

for row in tableHead:
    tableColumn = row.find_elements_by_tag_name('tr')
    rowQty = len(tableColumn)
    rowQty -= 1
    while rowQty >= 0:
        print(tableColumn[rowQty].get_attribute('innerText'))
        rowQty -= 1

print("----------")

print("TEST: Assert table rows read against expected.")
print("TEST: Collect and assert for all edit elements: HTML link as expected")
print("TEST: Collect and assert for all delete elements: HTML link as expected")

print("----------")
print("----------")

driver.implicitly_wait(2)
driver.quit()



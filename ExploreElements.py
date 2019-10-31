from selenium import webdriver
from time import sleep
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains
import re
from collections import defaultdict

driver = webdriver.Chrome("C:\Program Files (x86)\Python\WebDrivers\chromedriver.exe")
# driver = webdriver.Firefox()
# driver = webdriver.IE()

action = ActionChains(driver)

# TEST Setup --------------------------------------------------------------------------------------------------------

driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/challenging_dom")
driver.implicitly_wait(4)

# Discover Elements -----------------------

# Color properties for each button ---
# The below method should be evolved to a class ---

buttonElement = driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/a")
hexColorButton = buttonElement.value_of_css_property("background-color")
# print(Color.from_string(hexColorButton).hex)
action.move_to_element(buttonElement).perform()
driver.implicitly_wait(1)
hexColorButtonHover = buttonElement.value_of_css_property("background-color")
# print(Color.from_string(hexColorButtonHover).hex)
print("'Blue' Button color:", Color.from_string(hexColorButton).hex,
      "Hover color:", Color.from_string(hexColorButtonHover).hex)

buttonAlertElement = driver.find_element_by_class_name("button.alert")
hexColorAlert = buttonAlertElement.value_of_css_property("background-color")
# print(Color.from_string(hexColorAlert).hex)
action.move_to_element(buttonAlertElement).perform()
driver.implicitly_wait(1)
hexColorAlertHover = buttonAlertElement.value_of_css_property("background-color")
# print(Color.from_string(hexColorAlertHover).hex)
print("'Red' Alert.Button color:", Color.from_string(hexColorAlert).hex,
      "Hover color:", Color.from_string(hexColorAlertHover).hex)

buttonSuccessElement = driver.find_element_by_class_name("button.success")
hexColorSuccess = buttonSuccessElement.value_of_css_property("background-color")
# print(Color.from_string(hexColorSuccess).hex)
action.move_to_element(buttonSuccessElement).perform()
driver.implicitly_wait(1)
hexColorSuccessHover = buttonSuccessElement.value_of_css_property("background-color")
# print(Color.from_string(hexColorSuccessHover).hex)
print("'Green' Success.Button color:", Color.from_string(hexColorSuccess).hex,
      "Hover color:", Color.from_string(hexColorSuccessHover).hex)
print("----------")

print("TEST: Assert above color results against expected")

print("----------")
print("----------")
print("----------")

# Get Initial properties for buttons and canvas

getScript = driver.find_element_by_xpath("//div[@id='content']/script").get_attribute('innerHTML')
getAnswer = re.search(r"Answer:\s*(\d+)", getScript).group(1)

# getArray = re.split(r"[ ']+", getScript)
# print(len(getArray))
# getAnswer = getArray[16]
# print(getScript)

print("Initial Canvas element answer is :", getAnswer)

buttonElement = buttonElement.text
buttonAlertElement = buttonAlertElement.text
buttonSuccessElement = buttonSuccessElement.text
print("Initial text content of 3 buttons:", buttonElement, buttonAlertElement, buttonSuccessElement)
print("----------")
driver.implicitly_wait(2)

print("Assumption: Head, GitHub banner and footer static; ignoring these elements for this test")
print("TEST: Smoke test; initial presence/state/value of body elements")
print("TEST: Smoke test; assert content of Title and paragraph")
print("----------")
print("----------")
# Collect for "button"

# Collection lists for button
answerCollection = []
buttonBarCollection = []
buttonBazCollection = []
buttonFooCollection = []
buttonQuxCollection = []
buttonElseCollection = []
# final design can compress to fewer lists, likely two lists sufficient
i: int = 5
# method below should evolve to dictionary sort
while i >= 1:
    buttonElement = driver.find_element_by_class_name("button")
    canvasElement = driver.find_element_by_id("canvas")
    findText = buttonElement.text
    if findText == "bar":
        buttonBarCollection.append(buttonElement.id)
    elif findText == "baz":
        buttonBazCollection.append(buttonElement.id)
    elif findText == "foo":
        buttonFooCollection.append(buttonElement.id)
    elif findText == "qux":
        buttonQuxCollection.append(buttonElement.id)
    else:
        buttonElseCollection.append(buttonElement.id)

    getScript = driver.find_element_by_xpath("//div[@id='content']/script").get_attribute('innerHTML')
    getAnswer = re.search(r"Answer:\s*(\d+)", getScript).group(1)
    answerCollection.append(getAnswer)
    buttonElement.click()
    sleep(0.5)
    i -= 1

print("Bar:", buttonBarCollection)
print("Baz:", buttonBazCollection)
print("Foo:", buttonFooCollection)
print("Qux:", buttonQuxCollection)
print("Sneaky Elements:", buttonElseCollection, "   :For test pass this should be zero/empty")
print("----------")
print("QTY Canvas Answers:", len(answerCollection), "Answers:", answerCollection)
print("----------")

print("TEST: Assert above lists against expctd; All IDs unique and none outside expctd list(s) [Bar, Baz, Foo, Qux]")
print("TEST: collect and assert for button.alert")
print("TEST: collect and assert for button.success")

print("----------")
print("----------")
print("'Je n’ai fait celle-ci plus longue que parce que je n’ai pas eu le loisir de la faire plus courte.'")
print("Blaise Pascal, 1657")

sleep(2)
driver.quit()

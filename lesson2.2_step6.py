from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

xpathX = "//span[@id='input_value']"
xpathInput = "//input[@id='answer']"
xpathCheck = ""
xpathRadio = ""
calcValue = calc( browser.find_element_by_xpath( xpathX ).text )
input = browser.find_element_by_xpath(xpathInput)
input.send_keys(calcValue)

checkBox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()

radioButton = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", radioButton)
radioButton.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

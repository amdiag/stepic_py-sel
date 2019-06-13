from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
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
radioButton = browser.find_element_by_css_selector("[for='robotsRule']").click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

xpathX = "//span[@id='input_value']"
xpathInput = "//input[@id='answer']"
xpathRadio = ""
#calcValue = calc( browser.find_element_by_xpath( xpathX ).text )

imgElement = browser.find_element_by_id("treasure")
calcValue = calc( imgElement.get_attribute("valuex") )
input = browser.find_element_by_xpath(xpathInput)
input.send_keys(calcValue)

checkBox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
radioButton = browser.find_element_by_css_selector("[id='robotsRule']").click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

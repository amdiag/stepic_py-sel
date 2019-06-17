from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
first_window = browser.window_handles[0]

button = browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


xpathX = "//span[@id='input_value']"
xpathInput = "//input[@id='answer']"
xpathCheck = ""
xpathRadio = ""
calcValue = calc( browser.find_element_by_xpath( xpathX ).text )
input = browser.find_element_by_xpath(xpathInput)
input.send_keys(calcValue)

button = browser.find_element_by_css_selector(".btn.btn-primary").click()
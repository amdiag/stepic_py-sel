from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
#browser.implicitly_wait(5)                         # неявное ожидание, каждого элемента до 5 секунд
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))

button = browser.find_element_by_css_selector("button.btn")
button.click()

xpathX = "//span[@id='input_value']"
xpathInput = "//input[@id='answer']"
calcValue = calc( browser.find_element_by_xpath( xpathX ).text )

input = browser.find_element_by_xpath(xpathInput)
input.send_keys(calcValue)

button = browser.find_element_by_id("solve")
button.click()

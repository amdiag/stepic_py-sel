from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = int (browser.find_element_by_id("num1").text)
num2 = int (browser.find_element_by_id("num2").text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value((str)(num1 + num2)) # ищем элемент с текстом "Python"

button = browser.find_element_by_css_selector("button.btn")
button.click()

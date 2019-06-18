from selenium import webdriver
import time

browser = webdriver.Chrome()                    # неявное ожидание, каждого элемента до 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/cats.html")

browser.find_element_by_id("button")


#selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"button"}

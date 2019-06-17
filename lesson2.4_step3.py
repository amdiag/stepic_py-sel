from selenium import webdriver
import time

browser = webdriver.Chrome()                    # еявное ожидание, каждого элемента до 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")

#time.sleep(1)
button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text
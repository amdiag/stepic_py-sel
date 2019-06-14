from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
input1.send_keys("firstname")
input2 = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
input2.send_keys("lastname")
input3 = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
input3.send_keys("email")



current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = browser.find_element_by_css_selector("[id='file']")
element.send_keys(file_path)

button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        xpathFamily = "//div[2]//label[contains(text(),'Фамилия')]/../input"
        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath(xpathFamily)  # find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("third")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = browser.find_element_by_tag_name("h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Answer text isn't correct -" + welcome_text )

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        xpathFamily = "//div[2]//label[contains(text(),'Фамилия')]/../input"
        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath(xpathFamily)  # find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("third")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = browser.find_element_by_tag_name("h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Answer text isn't correct -" + welcome_text )

if __name__ == "__main__":
    unittest.main()

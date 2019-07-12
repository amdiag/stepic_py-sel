import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_check_url(browser, url):
    browser.get(url)
    txtArea = browser.find_element_by_tag_name('textarea')
    answer = math.log(int(time.time()))
    txtArea.send_keys(str(answer))
    # browser.find_element_by_xpath('//*[@id="ember1598"]')
    browser.find_element_by_class_name('submit-submission').click()
    txtValue = browser.find_element_by_class_name('smart-hints__hint').text
    assert txtValue == "Correct!", "Error - " + txtValue

    # time.sleep(1)
# //*[@id="ember1598"]          #ember1550
# //*[@id="ember1492"]/div/div/div[3]/div[2]/button[1]
# //*[@id="ember1670"]/pre

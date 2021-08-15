import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #step 1
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #step 2
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    #step 4
    x = browser.find_element_by_id("input_value")
    value = x.text
    y = calc(value)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #Ждем загрузки страницы
    time.sleep(1)

finally:
    #Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #Закрываем браузер после всех манипуляций
    browser.quit()
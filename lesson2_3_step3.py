import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #step 1
    link = " http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #step 2
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #step 3
    alert = browser.switch_to.alert
    alert.accept()

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
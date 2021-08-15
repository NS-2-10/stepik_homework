import math
from selenium import webdriver
import time

#step 3
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #step 1
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #step 2
    x = browser.find_element_by_id("treasure")
    value = x.get_attribute("valuex")
    y = calc(value)

    #step 4
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    #step 5
    option = browser.find_element_by_css_selector("#robotCheckbox")
    option.click()

    #step 6
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    #step 7
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #Проверяем, что смогли зарегистрироваться
    #Ждем загрузки страницы
    time.sleep(1)

finally:
    #Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #Закрываем браузер после всех манипуляций
    browser.quit()
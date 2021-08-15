import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

#step 3
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #sptep 1
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #step 2
    x = browser.find_element_by_id("input_value")
    value = x.text
    y = calc(value)

    #step 5
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)


    button = browser.find_element_by_css_selector("button.btn")
    #step 4
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #step 6
    option = browser.find_element_by_css_selector("#robotCheckbox")
    option.click()

    #step 7
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    button.click()

    #Ждем загрузки страницы
    time.sleep(1)

finally:
    #Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #Закрываем браузер после всех манипуляций
    browser.quit()
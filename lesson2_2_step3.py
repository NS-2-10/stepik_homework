from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    value1 = int(num1.text)
    value2 = int(num2.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(value1 + value2))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #Ждем загрузки страницы
    time.sleep(1)

finally:
    #Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #Закрываем браузер после всех манипуляций
    browser.quit()
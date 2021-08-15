import os 
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try: 
    #step 1
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #step 2
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
        element.send_keys("c:")

    #step 3
    browse = browser.find_element_by_css_selector('input[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'file.txt')           
    browse.send_keys(file_path)

    #step 4
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #Ждем загрузки страницы
    time.sleep(1)

finally:
    #Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #Закрываем браузер после всех манипуляций
    browser.quit()
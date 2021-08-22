from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #step 1
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #step 2
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    #step 3
    button = browser.find_element_by_id("book")
    button.click()  

    #step 4
    x = browser.find_element_by_id("input_value")
    value = x.text
    y = calc(value)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    #Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #Закрываем браузер после всех манипуляций
    browser.quit()
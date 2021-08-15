from selenium import webdriver
import time

try: 
    #Раскомментируйте строчку 6, а строчку 7 закомментируйте, если вам необходимо проверить тест на рабочей форме
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_class_name('form-control.first[required]')
    input1.send_keys('c:')
    input2 = browser.find_element_by_class_name('form-control.second[required]')
    input2.send_keys('c:')
    input3 = browser.find_element_by_class_name('form-control.third[required]')
    input3.send_keys('c:')
    

    #Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #Проверяем, что смогли зарегистрироваться
    #Ждем загрузки страницы
    time.sleep(1)

    #Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    #С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    #Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #Закрываем браузер после всех манипуляций
    browser.quit()
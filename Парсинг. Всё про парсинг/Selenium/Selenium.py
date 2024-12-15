import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
# browser.get('https://duckduckgo.com')  # Открываем страницу
# browser.save_screenshot('1.png')  # Делаем скриншот страницы
# time.sleep(5)
# browser.get('https://google.com')
# browser.refresh()  # Перезагрузка
# browser.quit()  # Выход из браузера

browser.get('https://www.vsemayki.ru/')
# 1 - часть
# Получение кнопки через XPATH и нажатие на неё
button = browser.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div[1]/div[2]/div/div[2]/div/a")
button.click()

# 2 - часть (чтобы работала, закомментируй 1 часть)
# Получение всех элементов (футболок) и вывод название их класса
time.sleep(10)
try:
    block = (browser.find_element(By.CLASS_NAME, "styles_content__3Wt6R").find_element(By.CLASS_NAME, "container")
             .find_element(By.CLASS_NAME, "row"))
    all_shorts = block.find_elements(By.CLASS_NAME, 'styles_catalog_list_card__3cP7c')
    for short in all_shorts:
        print(short.get_attribute('class'))
except BaseException:
    print("Чтобы код 2 части сработал закомментируй 1 часть")







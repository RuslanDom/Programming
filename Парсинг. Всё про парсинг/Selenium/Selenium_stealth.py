from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()  # Получаем опцию нашего браузера
options.add_argument('start-maximized')  # Аргумент для запуска в максимальном размере

# Параметры, которые делают наш браузер более реалистичным для сайта

options.add_experimental_option('excludeSwitches', ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Создание экземпляра нашего браузера
driver = webdriver.Chrome(options=options)
stealth(driver,
        languages=['en-US', 'en'],
        vendor='Google Inc.',
        platform='Win64',
        webgl_vendor='Intel Inc.',
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True
        )

url = "https://www.russiadiscovery.ru/tours/discovery-special/"
driver.get(url)

address_blocks = ["d-catalog__cards", "d-catalog__cards-group", "d-catalog__container-cards", "d-catalog__container"]

blocks = driver.find_element(By.CLASS_NAME, address_blocks[0])
all_block = blocks.find_elements(By.CLASS_NAME, "d-catalog__card")
for block in all_block:
    print(block.get_attribute('class'))

time.sleep(1500)







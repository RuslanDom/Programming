import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import re
""" В данной задачи я столкнулся с небольшой проблемой, вызванной ошибкой 403, я не мог получить доступ к сайту
    через bs4 даже используя fake_useragent, поэтому пришлось расширить знания парсинга и изучить библиотеки selenium,
    selenium_stealth """

# Я так понимаю что нужно было сделать что-то наподобие вот этого кода?
# Но этот вариант не работает из-за блокировки доступа
url = 'https://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
if response.status_code == 200:
    pattern = r'<h3.*?>(.*?)</h3>'
    res = re.findall(pattern, response.text)
    for elem in res:
        print(elem)
else:
    print(f"Status code: {response.status_code}")


# Рабочий вариант решения
def call_driver():
    options = webdriver.ChromeOptions()  # Получаем опцию нашего браузера
    options.add_argument('start-maximized')  # Аргумент для запуска в максимальном размере

    # Параметры, которые делают наш браузер более реалистичным для сайта
    options.add_experimental_option('excludeSwitches', ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)


    # Создание экземпляра нашего браузера
    my_driver = webdriver.Chrome(options=options)
    stealth(
        my_driver,
        languages=['en-Us', 'en'],
        vendor='Google Inc',
        platform='Win64',
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True)
    return my_driver


# В данном случае запрос request.get заменен на загрузку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()

# По итогу вы так же получаете код сайта в виде одной строки
# 1-й вариант
pattern = r'<h3>(.+)</h3>'
res = re.findall(pattern, text)
print(res)

# 2-й вариант
# При помощи bs4 парсим все теги h3 из файла
soup = BeautifulSoup(text, 'lxml')
h_3 = soup.find_all('h3')
print(h_3)

# При помощи библиотеки selenium и selenium_stealth получаем доступ к данным сайта и парсим все теги h3
driver = call_driver()
driver.get(url)
all_H3 = driver.find_elements(By.TAG_NAME, "h3")
for h3 in all_H3:
    print("Result:", h3.text)
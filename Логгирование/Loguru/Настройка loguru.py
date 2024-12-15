import sys

from loguru import logger
import requests
from bs4 import BeautifulSoup

logger.add(sys.stdout, format='{time} {level} {message}', level='TRACE')
# logger.add('logDebug.log', format='{time} {level} {message}', level='DEBUG', rotation='10KB', compression='zip')

url = "https://crossoutdb.com"
logger.debug(url)

response = requests.get(url)  # requests.get способ получения HTML с сайта
logger.debug(response)


# print(response.text) # Вывел текст всего сайта HTML


@logger.catch
def get_soup():
    return BeautifulSoup(response.text, "lxml")


# print(soup)


@logger.catch
def get_div(soup):
    return soup.find_all("div")  # .find и .find_all поиск по дереву HTML


get_div(get_soup())
logger.trace('---' * 30)
# Специально вызванная ошибка, передал объект функции, а не саму функцию
get_div(get_soup)


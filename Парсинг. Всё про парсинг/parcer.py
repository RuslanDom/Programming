import requests
from bs4 import BeautifulSoup

url = "https://crossoutdb.com"

response = requests.get(url) # requests.get способ получения HTML с сайта

# print(response.text) # Вывел текст всего сайта HTML

soup = BeautifulSoup(response.text, "lxml")

# print(soup)

data = soup.find_all("div") # .find и .find_all поиск по дереву HTML
print(data)




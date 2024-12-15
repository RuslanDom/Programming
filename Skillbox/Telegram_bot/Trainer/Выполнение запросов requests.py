import requests
from pprint import pprint
from Trainer.config_data import config
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'


def get_langs():
    response = requests.get(f'{BASE_URL}/getLangs', params={'key': API_KEY})
    return response


def lookup(lang, text, ui='ru'):
    response = requests.get(f'{BASE_URL}/lookup', params={
        'key': API_KEY,
        'lang': lang,
        'text': text,
        'ui': ui
    })
    return response


langs_response = get_langs()
if langs_response.status_code != 200:
    print('Не удалось получить список направлений перевода')
    exit(1)

langs = langs_response.json()
print("Выберите одно из доступных направлений перевода")
print(langs, "\n")
while (lang := input('Введите направление: ')) not in langs:
    print("Такого направления нет, попробуйте ещё раз")

text = input('Введите слово: ')
lookup_response = lookup(lang=lang, text=text)
if lookup_response.status_code != 200:
    print(f'Не удалось выполнить перевод: {text}')
    exit(1)

pprint(lookup_response.json())











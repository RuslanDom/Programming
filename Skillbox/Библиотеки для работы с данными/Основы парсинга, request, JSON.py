import requests
import json


link = requests.get("https://swapi.dev/api/people/1/")

# Переводим формат str в словарь dict
# loads(link.text) - работает с объектом парсинга
# load(file) - работает с файлом
# При помощи load() с файла json можно получить словарь
data = json.loads(link.text)  # Десериализация JSON
print(type(data))
print(data['name'])
data['skin_color'] = 'white'
print(data)
print('=' * 60)
# dump() - записывает данные в файл JSON
# dumps() - записывает данные в строку JSON в том числе html
json_D = json.dumps(link.text)
print(f"HTML страница в формате JSON: {json_D}")
with open('SWapi.json', 'w') as file:
    json.dump(data, file, indent=4)  # Сериализация объектов Python в объекты JSON

with open('SWapi.json', 'r') as file:
    data = json.load(file)  # Прочитаем json файл

print(data)

# Пример dumps()
different_data = ['text', False, {"0": None, 1: [1.0, 2.0]}]
json.dumps(different_data)
# Вывод: '["text", false, {"0": null, "1": [1.0, 2.0]}]'

employee_info = {"name": "John", "age": 35, "city": "San Francisco",
                 "home": "123 Main St.", "zip_code": 12345, "sex": "Male"}
print(json.dumps(employee_info, indent=2, sort_keys=True))  # sort_keys=True - ключи сортирует в алфавитном порядке

"""Если входные или выходные данные JSON являются строками, то они обозначаются буквой “s”. 
Поэтому мы присоединяем “s” к методу load. 
Таким же образом, если нам необходимы строки JSON, мы добавляем “s” к названию метода dump."""

with open('sw_templates.json', 'w') as f:
    json.dump(different_data, f)

# load()
with open('sw_templates.json', 'r') as f:
    templates = json.load(f)

print(templates)

# loads
with open('sw_templates.json', 'r') as f:
    file_content = f.read()
    templates = json.loads(file_content)

print(templates)


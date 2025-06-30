# Словари dict

dictionary = {1:"Number 1", 2: "Number 2", False: "Bool"}

man = {"Name": "Ruslan", "Age": 33, "isHappy":True}
print(man["Name"], man["Age"])

country = dict(code='RU', name='Russia', telCode='+7')

print(dictionary)

#Перебор словаря ключи и значения
for a, i in country.items():
    print(a, '-', i)

for key, value in man.items():
    print(key, " = ", value)


print(country.get('code'))
# man.clear()
# man.pop удалит ключ и значение
# man.popitem() удалит только последний элемент

print(man.keys())
print(man.values())
print(man.items())

# country.upload()  ==  country["code"] = "RUS"
country["code"] = "RUS" #Изменил значение элемента по ключу
print(country['code'])

pers = {
    'user_1': {
        "name": "John",
        "age": 40,
        "hobby": ["boxing", "run"]
    },
    'user_2': {
        "name": "John",
        "age": 30,
        "hobby": ["swiming", "walk", "tennis"]
    }
}
print(pers['user_2']['hobby'][2])

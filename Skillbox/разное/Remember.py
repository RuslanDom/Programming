from random import randint
all_student = int(input("Введите кол-во учеников: "))
normal = 0
good = 0
perfect = 0


"""Функция для того чтобы получить ключ словаря по значению"""


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


dict_stud = {"Троешники": 0, "Хорошисты": 0, "Отличники": 0}
for _ in range(1, all_student+1):
    grade = randint(3, 5)
    if grade == 3:
        normal += 1
    elif grade == 4:
        good += 1
    else:
        perfect += 1

dict_stud['троешников'] = normal
dict_stud['хорошистов'] = good
dict_stud['отличников'] = perfect
win = max(normal, good, perfect)
print(f'Больше всех {get_key(dict_stud, win)} их {win}')



"""-------------------------------------------- ЗАДАЧА ПРО ПИЦЦЫ --------------------------------------------"""
"""-------------------- Создание вложенного словаря из данных другого словаря -------------------"""

def form_order():
    all_numbers_order = int(input("Введите количество заказов: "))
    all_order = dict()
    for num in range(all_numbers_order):
        order = {'name': input("Введите имя: "),
                 'type': input("Введите название пиццы: "),
                 'count': int(input("Введите кол-во пиц: "))
                 }
        all_order[num] = order
    return all_order


def get_order(orders):
    result = {val['name']: {} for val in orders.values()}
    for i_res in result:
        for i_val in orders.values():
            if i_res == i_val['name']:
                result[i_res][i_val['type']] = i_val['count']

    print()
    for i_res in result:
        print(i_res, ":")
        for i in result[i_res]:
            print("     {}: {}".format(i, result[i_res][i]))


# ready_order = form_order()


ready_order = {
               0: {'name': 'Victor', 'type': 'Mexico', 'count': 3},
               1: {'name': 'Oleg', 'type': 'Mexico', 'count': 2},
               2: {'name': 'Victor', 'type': 'Europa', 'count': 1},
               3: {'name': 'Ivan', 'type': 'Mexico', 'count': 3},
               4: {'name': 'Victor', 'type': 'Asia', 'count': 4},
               5: {'name': 'Oleg', 'type': 'Asia', 'count': 5},
               }


get_order(ready_order)

"""--------------------------------hash функция--------------------------------"""


def hash_func(text):
    hash_value = 0
    for el in text:
        hash_value += ord(el)
    print(hash_value)
    return text


while True:
    play = hash_func(input("Enter text(для остановки введите - 'стоп'): "))
    if play == 'стоп':
        break
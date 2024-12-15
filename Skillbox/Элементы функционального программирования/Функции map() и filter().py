from typing import List

# map() принимает 2 аргумента, вторым передаём итерируемый объект, а первым действие которое с ним будет происходить
# на данном примере 2-ой аргумент список из строк разбитых через точку и 1-ый аргумент изменение str на int
date_string = '03.08.2024'
day, month, year = map(int, date_string.split('.'))
print(day, month, year)
# filter() отфильтровывает нужные значения
day1, month1, year1 = filter(str, date_string.split('.'))
print(day1, month1, year1)


my_nums: List[int] = [3, 1, 4, 1, 5, 8, 2]
other_nums: List[int] = [2, 7, 1, 8, 2, 8, 1, 8]

result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))  # Сложил оба списка my_nums и other_nums
print(result)  # Вывод: [5, 8, 5, 9, 7, 16, 3]

print(map(lambda x, y: x * y, [1, 2, 3], [1, 2, 3, 4, 5]))  # Вывод: <map object at 0x000002059964DA80>
print(list(map(lambda x, y: x * y, [1, 2, 3], [1, 2, 3, 4, 5])))  # Вывод: [1, 4, 9]

""" Функция map() против list comprehensions"""
animals = ['dog', 'cat', 'cow']

Capitalize_animal_map_lambda = list(map(lambda anim: anim.capitalize(), animals))
print(Capitalize_animal_map_lambda)  # Вывод: ['Dog', 'Cat', 'Cow']

Upper_animal_list_comprehensions = [ani.upper() for ani in animals]
print(Upper_animal_list_comprehensions)  # Вывод: ['DOG', 'CAT', 'COW']

""" Функция filter()"""
result_even = filter(lambda x: x % 2 == 0, result)
print(list(result_even))  # Вывод: [8, 16] только чётные числа от списка [5, 8, 5, 9, 7, 16, 3]

# отфильтровал my_nums по чётным числам и умножил их на 2
new_result = list(map(lambda x: x * 2, filter(lambda num: num % 2 == 0, my_nums)))
print(new_result)  # Вывод: [8, 16, 4]

""" Практика """
# Задача 1. Однострочный код
# Пользователь вводит неопределённое количество чисел.
# Напишите код, который запрашивает эти числа и сортирует их по возрастанию. Реализуйте решение в одну строку.

"""Пример работы консоли:
Введите числа: 5 8 4 1 0 3
[0, 1, 3, 4, 5, 8]"""
# res = sorted(filter(lambda num: num.isdigit(), input(" Введите числа:  ").split()))
# print(res)
# res_1 = sorted(map(lambda num: int(num), input(" Введите числа:  ").split()))
# print(res_1)
# res_2 = sorted(int(num) for num in input().split() if num.isdigit())
# print(res_2)

# Задача 2. Однострочный код 2
# Пользователь вводит строку, состоящую из любых символов.
# Напишите код, который выводит на экран список этих символов, исключая цифры и буквы в верхнем регистре.

"""Пример работы консоли:
Введите строку: qWe456rtY
['q', 'e', 'r', 't']"""


# res_str = filter(lambda letter: (letter.islower() and letter.isalpha()), input("Введите строку: "))
# res_str_2 = [i_let for i_let in input("Введите строку: ") if i_let.isalpha() and i_let.islower()]
# print(list(res_str))
# print(res_str_2)




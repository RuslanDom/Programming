import copy

# Списки list


list = [12,"Строка", False,22.2,[-1,-5,33,True],0]
list_2=[2,9,12,5,7,9,-2]

# обращение по индексу
# print(list_2[-1])
# print(list[1])
# print(list[-2])

# Можно присваивать другие значения по индексу
# list[0] = 21

data = [2,5,9]

list.append(111) # Можно добавлять новые элементы списка в его конец
list.insert(0,"Новый элемент") # Вставляет новый элемент по индексу
list.extend(data) # Добавляет
list_2.sort() # Сортирует
list.pop() # Можно удалять с индексом и без
list.remove("Строка") # Удаляет элемент по его значению
list_2.reverse() # Разворачивает список с начала на конец


# print(list.count(True)) Поиск по значению элемента выводит сколько раз данный элемент встречается в списке
# print(len(list)) Получаем длинну списка

# for i in list:
#     print(i)

# Эта программа сама создаёт список из 5 элементов с случайными числами от 0 до 100

import random
num = random.randint(0,100)
list_3 = []
i = 0
while i < 5:
    num = random.randint(0, 100)
    list_3.append(num)
    i += 1
print(list_3)

# Программа с ручным вводом данных списка

# le = int(input("Введите длинну списка: "))
# list_4 = []
# inx = 0
# while inx < le:
#     list_4.append(input("Введите элемент списка: "))
#     inx += 1
# for r in list_4:
#     print(r)



"""----------------------------------------------ПЕРЕВОРОТ СПИСКА----------------------------------------------"""

"""ЦИКЛОМ for"""
print("ПЕРЕВОРОТ СПИСКА")
first_list = [1, 2, 3, 4, 5]
print("Оригинальный список:", first_list)
reverse_list = []
for num in range(len(first_list) - 1, -1, -1):
    reverse_list.append(first_list[num])
print("Перевёрнутый список:", reverse_list)
"""Срезом"""
rev_list = first_list[::-1]
print("Перевёрнутый список при помощи среза rev_list = first_list[::-1]:", rev_list)
print()

"""-----------------------Метод deepcopy() -----------------------"""
print("-----------------------Метод deepcopy() -----------------------")
x = [1, 2, 3]
print('x = [1, 2, 3]')
print()
list_of_list = [x, 4, [4, 5, 6]]
list_of_list_2 = [x, [8], [7, 8, 9]]
print(list_of_list)
print(list_of_list_2)
print("\nИзменим list_of_list_2[0][0] = 10")
list_of_list_2[0][0] = 10
print(list_of_list)
print(list_of_list_2)
print('\nИспользуем метод copy.deepcopy()')
print('list_of_list_2 = copy.deepcopy(list_of_list)')
print('list_of_list_2[0][0] = 100')
list_of_list_2 = copy.deepcopy(list_of_list)
list_of_list_2[0][0] = 100
print(list_of_list)
print(list_of_list_2)

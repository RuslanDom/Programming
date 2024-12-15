from functools import reduce
from typing import List
# Задача 3. Функция reduce
# Помимо map и filter, есть ещё одна функция — reduce. Она применяет указанную функцию с 2 аргументами
# к элементам последовательности, return возвращает значение которое функция примет как 1-ый аргумент и
# 2-ым аргументом берёт следующее значение из полученных данных reduce(func - функция, data - итерируемые данные).


def my_add(a: int, b: int) -> int:
    result1 = a + b
    print(f"{a} + {b} = {result1}")
    return result1


# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 6 = 9
# 9 + 12 = 21
# 21
numbers: List[int] = [0, 1, 2, 6, 12]
print(reduce(my_add, numbers))

# Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке:
sentences = ["Nory was a Catholic", "because her mother was a Catholic",
             "and Nory’s mother was a Catholic", "because her father was a Catholic",
             "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"
             ]


def check_was(a, b):
    if isinstance(a, str):  # обработаем первый элемент отдельно
        a = int(a.count('was'))  # Считаем сколь раз повторяется was
    result2 = a + int(b.count('was'))
    return result2  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка


print(reduce(check_was, sentences))


# Решение без reduce()

def count_was(text):
    count = 0
    list_word = [word.rstrip(',') for word in ', '.join(text).split()]
    print(list_word)
    for i_word in list_word:
        if i_word == 'was':
            count += 1
    return count


print(count_was(sentences))

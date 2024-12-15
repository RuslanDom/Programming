from typing import List, Dict, Union

""" Данная функция аналогична lambda-функции"""
# def string_to_int(elem: str) -> int:
#     return int(elem[4:])  # Берём срез с 4 элемента строки, всё что после user...

# Example 1
users: List[str] = ['user10', 'user4', 'user3', 'user2', 'user6', 'user1', 'user8', 'user7', 'user9']
sorted_users = sorted(users, key=lambda elem_arg: int(elem_arg[4:]))  # Сортировка по ключу
print(sorted_users)

# Example 2
func = lambda num: num + 10
print(f'Результат Лямбда функции от (1): {func(1)}')

"""Задача 1 Минимум и максимум.
Мы знаем, что для нахождения минимального и максимального значений в наборе данных можно использовать
две встроенные функции: min() и max().И у них тоже можно использовать именованный аргумент key.
Скажем, дан вот такой список, в котором хранятся результаты соревнований в виде словарей:"""

grades: List[Dict[str, Union[str, int]]] = [{'name': 'Kenneth', 'score': 3},
                                            {'name': 'Bebe', 'score': 41},
                                            {'name': 'Joyce', 'score': 24},
                                            {'name': 'Richard', 'score': 37},
                                            {'name': 'Marian', 'score': 44},
                                            {'name': 'Jana', 'score': 45},
                                            {'name': 'Sarah', 'score': 90},
                                            {'name': 'Eddie', 'score': 2},
                                            {'name': 'Mary', 'score': 63},
                                            {'name': 'Ronald', 'score': 15},
                                            {'name': 'David', 'score': 44},
                                            {'name': 'Richard', 'score': 78},
                                            {'name': 'Warren', 'score': 7},
                                            {'name': 'Alyssa', 'score': 13}
                                            ]

print(grades[1]['name'])
result_max = max(grades, key=lambda data: [data['score'] for _ in data])
print(f'Самая большая оценка: {result_max}')
result_min = min(grades, key=lambda data: [data['score'] for _ in data])
print(f'Самая маленькая оценка: {result_min}')

test = lambda elem: [elem[i]['name'] for i in range(len(elem))]  # Получил все имена из списка словарей
print(test(grades))
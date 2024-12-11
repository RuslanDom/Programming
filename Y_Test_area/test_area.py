import functools
from typing import List
import os
from random import sample
from sys import getsizeof

print("Sample из random")
collection = [1, 3, 5, 9, 21, 45, 76, 63, 8]
r = sample(collection, 4)
res = [(i, ) for i in sample(range(1000), 5)]
print(r)
print(res)


print("---+++---" * 8)
print("Размеры структур данных")
s = {1, 'red', (1, 5, 7), 'green', 6, (12, "grey"), 'yellow', False}
l = [1, 'red', (1, 5, 7), 'green', 6, (12, "grey"), 'yellow', False]
t = (1, 'red', (1, 5, 7), 'green', 6, (12, "grey"), 'yellow', False)


print(f"Set Множество: {getsizeof(s)} байт")
print(f"List Список: {getsizeof(l)} байт")
print(f"Tuple Кортеж: {getsizeof(t)} байт")
print(f"Размер файла с использованием os.path.getsize(): {os.path.getsize('create_file_with_words.py')} байт")

print("---+++---" * 8)
print('Пример работы функции reduce()')
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list)
def num_sum(a, b):
    return a + b
result = functools.reduce(num_sum, num_list)
print("Результат reduce:", result)

print("---+++---" * 8)
print("Генератор yield")
def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

for i in partition(l, 2):
    print(i)

print("---+++---" * 8)
import hashlib
h = hashlib.sha1(b"my password")
print(h.hexdigest())
print(h.digest())

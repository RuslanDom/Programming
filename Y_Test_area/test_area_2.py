# from itertools import cycle
#
# def xor(message, key):
#     return bytes(a ^ b for a, b in zip(message, cycle(key)))




# key = b'key'
# value = 'hello world'
# print(value)
# res = xor(value.encode(), key)
# answer = xor(res, key).decode()
#
# print(res)
# print(answer)



# password = input("pass: ")
# if any(p.isdigit() for p in password):
#     print("Есть число")
# else:
#     print("Числа нет")
# print([p.isdigit() for p in password])

# department = input('dep: ')
# departments = {"IT": "it_dept", "PROD": "production_dept"}
# dept_directory_name = departments.get(department)  # Получаем значение по ключу
# print(dept_directory_name)
#
# import logging
# import json
#
#
# class JsonAdapter(logging.LoggerAdapter):
#     def process(self, msg, kwargs):
#
#
#         new_message = json.dumps(msg, ensure_ascii=False)
#         return new_message, kwargs
#
#
# if __name__ == '__main__':
#     logging.basicConfig(
#         level=logging.DEBUG,
#         datefmt='%H:%M:%S',
#         format='"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"'
#     )
#     logger = JsonAdapter(logging.getLogger(__name__))
#     logger.setLevel(logging.DEBUG)
#     logger.info('Сообщение')
#     logger.error('Кавычка)"')
#     logger.debug("Еще одно сообщение")






"""
SELECT DISTINCT battle
FROM Outcomes
JOIN Ships ON Ships.name = Outcomes.ship
WHERE Ships.class = 'Kongo'
"""

"""
SELECT name FROM Ships
WHERE name = class
UNION
SELECT ship FROM Classes, Outcomes
WHERE Outcomes.ship = Classes.class
"""

"""
SELECT DISTINCT ship
FROM Outcomes 
INTERSECT 
SELECT DISTINCT class
FROM Classes
UNION
SELECT DISTINCT class 
FROM Classes
"""

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(7))
"""
SELECT DISTINCT class FROM Ships
UNION
SELECT DISTINCT ship FROM Outcomes
WHERE ship IN (SELECT class from Classes)
"""
from typing import List

N: int = int(input("Number limit: "))
A: List[bool] = [True] * N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        A[k]
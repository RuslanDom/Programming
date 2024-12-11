from curses.ascii import isdigit
from itertools import cycle

def xor(message, key):
    return bytes(a^b for a, b in zip(message, cycle(key)))

# key = b'key'
# value = 'hello world'.encode()
# print(value.decode())
# res = xor(value, key)
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

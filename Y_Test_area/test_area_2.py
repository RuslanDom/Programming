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












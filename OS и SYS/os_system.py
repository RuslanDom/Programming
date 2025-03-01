
# Python позволяет нам немедленно выполнить команду оболочки, которая хранится в строке, используя функцию os.system().

import os

# result = os.system('ps -e | grep "/ps"')
result = os.system('ps -u ruslan')
# print("Результат: {}".format(result))
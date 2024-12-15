"""Программа для записи в тестовый документ истории поиска"""
import os


def search_file(direct, file):
    """ 1 - Написать цикл для генерации пути
        2 - Проверить на соответствие файл и конечного элемента пути, если ДА возвращаем верный путь
        3 - Делаем рекурсию для проверки вложенных элементов
        4 - При помощи ветвления блока if else останавливаем рекурсию и возвращаем полученное значение
    """
    for i_elem in os.listdir(direct):
        path = os.path.join(direct, i_elem)
        if file == i_elem:
            return path
        elif os.path.isdir(path):
            result = search_file(path, file)
            if result:
                break
    else:
        result = None
    return result


file_name = input("Введите искомый файл: ")
res = search_file(os.path.abspath(os.path.join('../..', '..', 'Programming')), file_name)
history_file = open('history_search.txt', 'a')
print(res)
if res:
    print('Файл найден')
    history_file.write(res + '\n')
else:
    print('Такого файла нет')
history_file.close()
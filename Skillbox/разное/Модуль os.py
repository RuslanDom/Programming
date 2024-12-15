import os
folder_name = 'image'
file_name = 'disc-cat.png'
way = 'docs/{folder}/{file}'.format(
    folder=folder_name,
    file=file_name
)
print(way)

"""path.join с модуль os строит относительный путь в разных ОС"""
rel_way = os.path.join('docs', folder_name, file_name)
print(rel_way)

"""path.abspath находит абсолютный путь до файла"""
abs_path = os.path.abspath(file_name)
print(abs_path)

"""Подниматься в папку выше через команду"""
os.path.abspath(os.path.join('../..', file_name))

"""Подниматься в корневую папку"""
os.path.abspath(os.path.join(os.path.sep, file_name))

"""Функция listdir()"""
def print_path(project):
    for i_el in os.listdir(project):
        path = os.path.join(project, i_el)
        print(path)


print_path(os.path.abspath(os.path.join('../..', "Python")))
print()
print(os.path.abspath(os.path.join('access', 'admin.bat')))
print(os.path.join('Sckillbox', 'access', 'admin.bat'), '\n')


"""Поиск файла с помощью рекурсии"""
def find_file(current_path, file_name):
    print('Переходим', current_path)


    for i_elem in os.listdir(current_path):
        path = os.path.join(current_path, i_elem)
        print('    Смотрим путь', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print("Эта директория")
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result

file_path = find_file(os.path.abspath
                      (os.path.join('../..', 'Skillbox')),
                      'task_1.py')
if file_path:
    print("Абсолютный путь к файлу", file_path)
else:
    print("Файл не найден")



"""Алгоритм поиска любого файла, папки или ссылки(для файла выводится его размер)"""
def search_obj(abs_path_user, file_user):
    print('Ищем в ', abs_path_user)
    for i_elem in os.listdir(abs_path_user):
        path = os.path.join(abs_path_user, i_elem)
        print("     Просматриваем данный путь", path)
        if file_user == i_elem:
            if os.path.isdir(path):
                print('         Это папка')

            elif os.path.isfile(path):
                print('         Это файл')
                print('         Его размер', os.path.getsize(path))

            elif os.path.islink(path):
                print('         Это ссылка')
            return path
        elif file_user != i_elem:
            if os.path.isdir(path):
                res = search_obj(path, file_user)
                if res:
                    break
    else:

        res = None
    return res


file_user = input("Введите название объекта который ищите: ")
search_obj(os.path.abspath(os.path.join('../..', '..', 'Programming')), file_user)
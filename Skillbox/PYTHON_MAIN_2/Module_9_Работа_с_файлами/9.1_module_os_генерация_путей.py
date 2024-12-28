import os

folder_name = 'project'
file_name = 'my_file.txt'
print('---***---' * 5)

"""
    1. Генерация относительного пути с помощью os.path.join()
"""
real_path = os.path.join('docs', folder_name, file_name)
print(real_path)
print('---***---' * 5)

"""
    2. Генерация абсолютного пути с помощью os.path.abspath()
"""
# Генерирует путь до не существующего файла в данном случае
# Абсолютный путь будет составлен с учётом откуда запущен код
print("Абсолютный путь")
abs_path = os.path.abspath(__file__)
print(abs_path)

print("\nПримеры перемещения по path:")
path_1up = os.path.abspath(os.path.join('..', file_name))
print(f"\tНа 1 позицию вверх == {path_1up}")
path_2up = os.path.abspath(os.path.join('..', '..', file_name))
print(f"\tНа 2 позиции вверх == {path_2up}")
path_root = os.path.abspath(os.path.join(os.path.sep, file_name))
print(f"\tПуть с коневой папки == {path_root}")
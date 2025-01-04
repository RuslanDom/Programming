import os
from typing import Dict, Any


def find_file(cur_path: Dict or Any, filename):
    print("переходим в", cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print(f"\tсмотрим путь {path}")
        if filename == i_elem:
            return path
        if os.path.isdir(path):
            print('эта директория')
            result = find_file(path, filename)
            if result:
                print("Success!")
                break
    else:
        result = None
    return result


file_path = find_file(
    cur_path=os.path.abspath(os.path.join('..', '..', '..', 'Skillbox')),
    filename='http_utils.py'
)


history_file = open('search_history.txt', 'a')
if file_path:
    print(f"Абсолютный путь к искомому файлу: {file_path}")
    history_file.write(file_path + '\n')
else:
    print("Файл не найден.")
history_file.close()


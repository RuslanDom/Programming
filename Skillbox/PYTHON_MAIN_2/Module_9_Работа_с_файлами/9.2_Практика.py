import os, sys


def search_path_on_exists(path: str):
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f"This is file\nSize file: {sys.getsizeof(path)}")
            return True
        elif os.path.isdir(path):
            print(f"This is dir")
    else:
        print(f"{path} is not exists")

        # Рекурсивный поиск до первого файла
        # root_path = os.path.dirname(path)
        # print("Dir name: ", root_path)
        # for elem in os.listdir(root_path):
        #     search_path_on_exists(os.path.join(root_path, elem))
    return False


check_path = os.path.abspath(os.path.join('..', '..', input('Enter file: ')))

result = search_path_on_exists(check_path)


# Получение имя папки, где содержится файл

# path = os.path.abspath('9.2_Практика.py')
# dir_name = os.path.dirname(path)
# print(dir_name)









import os


path_under_consideration = ['Skillbox', 'Python']


def view_listdir_on_the_way(path):
    for i_elem in os.listdir(path):
        every_way = os.path.join(path, i_elem)
        # print(f"\t{i_elem}")  # только сами элементы
        print(f"\t{every_way}")  # пути до каждого элемента



def select_paths(element_to_path):
    for el in element_to_path:
        path = os.path.abspath(os.path.join('..', '..', '..', el))
        print(f"\nДиректория {path} содержит:")
        view_listdir_on_the_way(path)


if __name__ == '__main__':
    select_paths(path_under_consideration)

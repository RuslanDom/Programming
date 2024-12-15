import os.path
import time


class Timer:
    def __init__(self) -> None:
        print("Время работы кода")
        self.start = None

    def __enter__(self) -> "Timer":
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(time.time() - self.start)
        # if exc_type in TypeError:  # Пропускает только ошибку TypeError
        #     return True
        return True  # Позволяет пропустить все возникающие ошибки


with Timer() as t1:
    print("Первая часть")
    val_1 = 100 * 100 ** 1000000
with Timer() as t2:
    print("Вторая часть")
    val_2 = 200 * 200 ** 1000000
with Timer() as t3:
    print("Третья часть")
    val_3 = 300 * 300 ** 1000000


"""Свой файловый менеджер"""


class File:
    def __init__(self, name, mode):
        self.name_file = name
        self.mode = mode
        self.data = None

    def __enter__(self):
        path = os.path.abspath(f'{self.name_file}')
        self.data = open(path, 'w', encoding='utf-8')
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if exc_type is TypeError:
        #     self.data.close()
        #     return True
        self.data.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!')


""" Создание класса для контекст менеджера with..as
__enter__ и __exit__ оборачивают код который выполняется в теле with..as """


class Timer2:
    def __init__(self):
        self.result = None

    def __enter__(self):
        self.start = time.time()
        print("Этот код выполнится перед телом with")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Этот код выполняется после тела with")
        print(f'Функция выполненная в классе {Timer.__name__}: за {round(time.time() - self.start, 5)} секунд(ы)')
        return True


def squares_summa():
    res = 0
    for _ in range(1000):
        res += sum(i_num ** 2 for i_num in range(1000))
    return res


print()
with Timer2() as t4:
    print("Тут идёт выполнение функции! Находящейся код в теле with..as")
    result = squares_summa()
    print(f'Итог вычисления функции {result}')


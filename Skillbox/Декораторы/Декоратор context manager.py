import time
from contextlib import contextmanager
from collections.abc import Iterator

# @contextmanager для создания структуры with..as заменяет написание класса с методами __enter__ и __exit__
# на написание функции - генератора, код до yield выполняется как в __enter__ после yield как в __exit__


@contextmanager
def next_num(num: int) -> Iterator[int]:
    print("Входим в функцию")
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print("Обнаружена ошибка", exc)
    finally:
        print("Здесь код выполнится в любом случае")
    print("Выход из функции")


with next_num(-1) as next:
    print("Следующее число = {}".format(next))
    print(10 / next)


""" Context manager в виде функции - генератора timer() вместо class Timer """


# class Timer:
#     def __init__(self) -> None:
#         print("Время работы кода")
#         self.start = None
#
#     def __enter__(self) -> 'Timer':
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(time.time() - self.start)
#         return True

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(time.time() - start)


with timer() as t1:
    print("Первая часть")
    val_1 = 100 * 100 ** 10000

with timer() as t2:
    print("Первая часть")
    val_2 = 200 * 200 ** 20000


with timer() as t3:
    print("Первая часть")
    val_3 = 300 * 300 ** 30000
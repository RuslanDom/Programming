import time
import functools
from typing import Callable, Any

# Callable - это функция как ОБЪЕКТ например squares_sun или cubes_sum без ()

def timer(func: Callable) -> Callable:
    """
    Декоратор, выводящий время выполнение декорируемой функции
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'Работает декоратор timer!')
        started_time = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_time, 4)
        print(f'Функция работала {run_time} секунд(ы)')
        return result

    return wrapped_func


def logging(func: Callable) -> Callable:
    """
    Декоратор логирующий работу кода
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'Вызывается функция {func.__name__}\t'
              f'Позиционные аргументы: {args}\t'
              f'Именнованные аргументы: {kwargs}')
        result = func(*args, **kwargs)
        print("Функция завершила работу")
        return result

    return wrapped_func


"""
Порядок декорирования имеет значение
"""


@logging
@timer
# logging(timer(func))
def squares_sun() -> int:
    """
    Функция подсчёта квадратов суммы чисел
    :return: возвращает результат суммы
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


@timer
@logging
# timer(logging(func))
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result


my_sum = squares_sun()
print(my_sum)
print(squares_sun.__name__)
print(squares_sun.__doc__)

my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)

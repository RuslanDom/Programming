import time
from typing import Callable, Any


def timer(func: Callable, *args, **kwargs) -> Any:
    """ Функция - таймер, является функцией высшего порядка,
        потому что получает в качестве параметра другую функцию"""
    started_time = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_time, 4)
    print(f'Функция работала {run_time} секунд(ы)')
    return result


def squares_sun() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
    return result


my_result = timer(squares_sun)
my_cubes_sum = timer(cubes_sum, 200)
print(my_result)
print(my_cubes_sum)

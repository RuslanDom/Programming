import time
from collections.abc import Callable
import functools

""" 
    Добавляем новый аргумент precision (для обозначения кол-ва знаков при округлении после запятой)в декоратор,
    для это требуется обернуть старый декоратор ещё в одну функцию
    которая и примет новый аргумент;
    _func=None позволяет запускать декоратор без использования (),
    оператор * означает что все аргументы декоратора должны передаваться как именованные аргументы
"""


def timer_with_precision(_func=None, *, precision=3) -> Callable:
    def timer_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            time_work_func = round(time.time() - start, precision)
            print(f'Функция {func.__name__} выполнилась за {time_work_func}секунд(ы)')
            return result
        return wrapped_func
    if _func is None:
        return timer_decorator
    return timer_decorator(_func)


@timer_with_precision(precision=4)
def squares_summa() -> int:
    res = 0
    for _ in range(1000):
        res += sum(i_num ** 2 for i_num in range(10000))
    return res


@timer_with_precision
def cubes_summa() -> int:
    res = 0
    for _ in range(1000):
        res += sum(i_num ** 3 for i_num in range(10000))
    return res


squares_summa()
cubes_summa()
print()


def args_for_freezing_time(_func=None, *, seconds_sleep: int = 3):
    def freezing_time(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Код начала обертки")
            time.sleep(seconds_sleep)
            result = func(*args, **kwargs)
            print(f'Функция {func.__name__} выполниласть. Ответ: {result}')
            print("Код обертки после выполнения функции")
            return result
        return wrapper
    if _func is None:
        return freezing_time
    else:
        return freezing_time(_func)


@args_for_freezing_time(seconds_sleep=5)
def new_func_squares_summ():
    print("Выполняется функция {func}".format(func=new_func_squares_summ.__name__))
    result = 0
    for _ in range(100):
        result += sum(i ** 2 for i in range(1000))
    return result


new_func_squares_summ()



import functools
from datetime import datetime
import time
from typing import Callable

""" Декоратор класса может удалять, добавлять, переименовывать, изменять методы и атрибуты класса, 
    фактически он может возвращать абсолютно другой класс
"""


def create_time(cls):
    """ Декоратор выводит время создания инстанса класса"""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'Время создания класса {cls.__name__}: {datetime.now()}')
        return instance
    return wrapper


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Время работы {func.__name__}: {round(time.time() - start, 3)}")
        return result
    return wrapper


def for_all_methods_cls(decorator: Callable) -> Callable:
    """ Декоратор класса,
        который получает другой декоратор и применяет его ко всем методам класса"""
    @functools.wraps(decorator)
    def decorate(cls):
        # Метод dir() позволяет получить все методы класса
        # print(dir(cls)) - Выведет все названия методов класса
        for i_method_name in dir(cls):
            # Отсеиваем все магические методы
            if i_method_name.startswith('__') is False:
                # Получаем нужный метод класса
                need_method = getattr(cls, i_method_name)
                # Применяем декоратор @timer к нужному методу класса
                decorated_method = decorator(need_method)
                # Заменяем старый метод класса на новый за декорированный метод
                # Причём меняем через имя метода i_method_name
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@create_time
@for_all_methods_cls(timer)
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_num)])
        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])
        return result


my_f1 = Functions(max_num=1000)
time.sleep(1)
my_f2 = Functions(max_num=2000)
time.sleep(1)
my_f3 = Functions(max_num=3000)

my_f1.squares_sum()
my_f1.cubes_sum(number=1000)


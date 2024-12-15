from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()


def register(func: Callable) -> Callable:
    """Декоратор регистрирует функцию как плагин"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    """
    Функция приветствия!
    :param name: имена объекта которого приветствует функция
    :return: Строка приветствия
    """
    return "Hello {name}".format(name=name)


@register
def say_bye(name: str) -> str:
    return "Goodbye {name}".format(name=name)


print(PLUGINS)
print(say_hello('Tom'))
print(say_hello.__doc__)

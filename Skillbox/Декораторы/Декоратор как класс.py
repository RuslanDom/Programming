from typing import Callable
import functools


class DecoratorCountCalls:
    """ В классе декораторе init должен всегда хранить ссылку на декорируемую функцию"""
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0
    """ Для того чтобы сделать из класса декоратор нужно использовать специальный магический метод __call__
        позволяет вызову экземпляра класса быть вызванным как будто он функция Х() то же самое что Х.__call__
        суть метода такая же как у функции wrapper()
    """
    def __call__(self, *args, **kwargs) -> Callable:
        self.calls += 1
        print(f'Вызов номер {self.calls} функции {self.func.__name__}')
        return self.func(*args, **kwargs)


@DecoratorCountCalls
def say_hello():
    print('Hello')


say_hello()
say_hello()
say_hello()
# Можно обратится к полям класса - декоратора
print(say_hello.calls)

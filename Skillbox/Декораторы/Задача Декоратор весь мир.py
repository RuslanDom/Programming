from typing import Callable


def decorator_with_args_for_any_decorator(func_decorate: Callable):
    def wrapper_decorate(*args, **kwargs):
        def wrapper(func):
            return func_decorate(func, *args, **kwargs)
        return wrapper
    return wrapper_decorate


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args_dec, **kwargs_dec):
    def wrapper(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: ({args_dec, kwargs_dec})')
        return func(*args, **kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
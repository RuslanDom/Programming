# from functools import lru_cache


def catch_funk(func):
    res_catch = dict()

    def wrapped(*args, **kwargs):
        if args in res_catch:
            return res_catch[args]
        else:
            result = func(*args, **kwargs)
            res_catch[args] = result
            return result
    return wrapped


# Возможно такое решение через модуль functools @lru_cache(maxsize=None)
@catch_funk
def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(5))

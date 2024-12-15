def f1():
    print(f'В f1 number={number}')


def f2():
    number = 200  # Локальная переменная
    print(f'В f2 number={number}')


def f3():
    def f4():
        # global number - использует глобальную переменную
        nonlocal number  # nonlocal использует переменную из enclosing score
        number = 400
        print(f'В f4 number={number}')

    number = 300
    print(f'В f3 number={number}')
    f4()
    print(f'В f3 number после выполнения f4={number}')


number = 100
print(f'Глобальная переменная: {number}')
# f1()
# f2()
# f3()


""" Задача подсчёт вызова функции """

import functools
calls = 0


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        global calls
        calls += 1
        print(f'Функция {self.func.__name__} выведена {calls} раз(а)')
        return self.func(*args, **kwargs)



@CountCalls
def f1():
    print(f'В f1 number={number}')


# f1()
f1()
print(f'Методы и функции встроенного пространства: {dir(CountCalls)}')
print(f'Методы и функции встроенного пространства: {dir(f1)}')

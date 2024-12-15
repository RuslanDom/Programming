def factorial(number):
    """ Условие if здесь точка остановки рекурс ии"""
    if number == 1:
        return 1
    fact = factorial(number - 1)
    return number * fact


""" Формула n! = n * (n! - 1)
    т.е.    5! = 5 * 4!
            4! = 4 * 3!
            3! = 3 * 2! и т.д."""

num = int(input("Введите число для подсчёта его факториала: "))
print("Факториал числа {}! равен {}".format(num, factorial(num)))
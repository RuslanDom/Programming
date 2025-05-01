import sys

"""
Рекурсия матрёшки
"""
def matryoshka(n):
    if n == 1:
        print("Матрёшечка")
    else:
        print("Верх матрёшки")
        matryoshka(n - 1)
        print("Низ матрёшки")

# Вызов примера 1
# matryoshka(5)

"""
Фрактал квадратов
"""
import pygame as pg
pg.init()

class Fractale:
    def __init__(self):
        self.window = pg.display.set_mode((600, 600))
        self.ALPHA = 0.2

    def fractale_rectangle(self, A: tuple, B: tuple, C: tuple, D: tuple, deep=5):
        if deep < 1:
            return
        for M, N in [(A, B), (B, C), (C, D), (D, A)]:
            pg.draw.line(
                surface=self.window,
                color=(0, 0, 0),
                start_pos=M,
                end_pos=N,
                width=2
            )
        A1 = (A[0] * (1 - self.ALPHA) + B[0] * self.ALPHA, A[1] * (1 - self.ALPHA) + B[1] * self.ALPHA)
        B1 = (B[0] * (1 - self.ALPHA) + C[0] * self.ALPHA, B[1] * (1 - self.ALPHA) + C[1] * self.ALPHA)
        C1 = (C[0] * (1 - self.ALPHA) + D[0] * self.ALPHA, C[1] * (1 - self.ALPHA) + D[1] * self.ALPHA)
        D1 = (D[0] * (1 - self.ALPHA) + A[0] * self.ALPHA, D[1] * (1 - self.ALPHA) + A[1] * self.ALPHA)
        self.fractale_rectangle(A1, B1, C1, D1, deep - 1)

    def run(self):
        while True:
            self.window.fill((220, 255, 220))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                self.fractale_rectangle(
                    A=(100, 100),
                    B=(500, 100),
                    C=(500, 500),
                    D=(100, 500),
                    deep=10
                )
                pg.display.update()

# Вызов примера 2
# Fractale().run()

"""
Факториал
"""
def factorial(n):
    # Оператор проверки assert
    assert n >= 0, "Факториал отрицательного числа не определён"
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Вызов примера 3
n = 5
f = factorial(n)
print("Факториал числа {}! = {}".format(n, f))

"""
Алгоритм Евклида
Эффективный алгоритм для нахождения наибольшего общего делителя двух целых чисел (или общей меры двух отрезков).
"""

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)

def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a % b)


# Вызов примера 4
a, b = 9, 3
g = gcd(a, b)
g2 = gcd_2(a, b)
print("Наибольший общий делитель чисел {} и {}: {}".format(a, b, g))
print("Наибольший общий делитель чисел {} и {}: {}".format(a, b, g2))

"""
Быстрое возведение в степень
"""

def my_pow(a: float, n: int):
    if n == 0:
        return 1
    return my_pow(a, n - 1) * a

def my_pow_2(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return my_pow_2(a ** 2, n // 2)
    return my_pow_2(a, n - 1) * a

n = 11
a = 2

mp = my_pow(a, n)
mp2 = my_pow_2(a, n)
print("Возведение числа {} в степень {} равно {}".format(a, n, mp))
print("Возведение числа {} в степень {} равно {}".format(a, n, mp2))




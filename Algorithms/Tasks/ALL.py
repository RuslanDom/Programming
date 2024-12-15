"""Из всех введенных чисел берёт 2 самых больших и выводит их"""

N = int(input("Какое кол-во чисел будет сравниваться? "))
first_num = 0
second_num = 0
middle_num = 0
for item in range(N):
    num = int(input('Введите число: '))

    if num > first_num and num > second_num:
        if item > 0:
            if middle_num > first_num:
                first_num = middle_num
        middle_num = num
        second_num = num
    elif num > first_num:
        first_num = num

print(first_num, second_num)

"""Пирамида"""

rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == rows - j + 1:
            print("* " * i, end='')
        else:
            print(' ', end='')
    print()
    """         *
               * *
              * * *
             * * * *
            * * * * *
           * * * * * *
          * * * * * * *
         * * * * * * * *
        * * * * * * * * *
       * * * * * * * * * *   """

N = int(input("Введите высоту: "))
An = 1 + 2 * (N - 1)

for row in range(1, N + 1):
    for col in range(An):
        if row == - col + N:
            print("#" * (1 + 2 * (row - 1)), end='')
        else:
            print(" ", end='')
    print()

    #
    ###
    #####
    #######

"""Пирамида из нечётных чисел по заданному кол-ву рядов"""
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

row = int(input("Введите уровень: "))
num_in_row = 1
value = 1
for i in range(1, row + 1):
    for j in range(0, row):
        if i == -j + row:
            for num in range(num_in_row):
                print(value, "  ", end='')
                value += 2

        else:
            print("  ", end='')
    num_in_row += 1
    print()

"""Яма"""

# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345


row = int(input("Введите уровень: "))
col = row * 2

num = 1
for r in range(0, row):
    for c in range(0, col):
        if c <= r:
            print(row - c, end='')
        elif c >= col - 1 - r:
            print(c - row + 1, end='')

        else:
            print('.', end='')

    print()

"""Другое решение задачи ЯМА"""
rows = int(input("Введите уровень: "))

for row in range(1, rows + 1):
    for col in range(rows, rows - row, -1):
        print(col, end='')

    for col in range(rows * 2 - row * 2):
        print('.', end='')

    for col in range(rows + 1 - row, rows + 1):
        print(col, end='')

    print()

"""------------FUNCTION--------------"""


def func_a(num_a, num_b):
    finish_result = 0
    start_b = 1
    for num in range(1, num_a + 1):
        if num_a % num == 0:
            temp = num
            res = func_b(start_b, num_b)
            if temp == res:
                finish_result = temp
        start_b += 1
    print(f'Самый большой общий делитель: {finish_result}')


def func_b(start, number_b):
    result = 0
    for num in range(start, number_b + 1):
        if number_b % num == 0:
            if num > result:
                result = num
                return result


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

func_a(a, b)

"""Плавающая точка"""
# Пример 1:
#
# Введитечисло: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
#
# Пример 2:
#
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

x = float(input('Введите число: '))
a = x
count = 0
if x > 1:
    while 1 > a or a > 10:
        count += 1
        a /= 10
    x = a

    print(f'Формат плавающей точки: x = {x} * 10 ** {count}')

else:
    while 1 > a:
        count += 1
        a *= 10
    x = x * 10 ** count
    print(f'Формат плавающей точки: x = {x} * 10 ** -{count}')

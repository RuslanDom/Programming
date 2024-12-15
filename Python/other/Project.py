print('Hello world')
# Игра угадай число
# Загадывается секретное число в диапозоне 1-20 и просит угадать это число,
# после каждой попытки сообщает больше или меньше это число загаданного,
# выиграет пользователь если угадает с 3 раз

import random

print('Добро пожаловать в игру "Угадай число"')
print('Попробуйте угадать число от 1 до 20, у вас есть 3 попытки')
numb = random.randint(1, 20)

chance = 0
for chance in range(3):
    variant = input('Введите число: ')
    variant = int(variant)

    if variant == numb:
        break

    if variant > numb:
        print('Слишком много попробуй число по меньше')

    if variant < numb:
        print('Слишком мало попробуй число по больше')

if variant == numb:
    chance = str(chance + 1)
    print('Верное число, ты угадал, у тебя получилось с ' + chance + ' попытки')

if variant != numb:
    numb = str(numb)
    print('Ты исчерпал все попытки и не угадал, попробуй в следующий раз, загаданным числом было число - ' + numb)


fruits = ['lemon', 'pear', 'watermelon', 'tomato']

print(fruits[0], fruits[1], fruits[2], fruits[3])
# lemon pear watermelon tomato
print(*fruits)
# lemon pear watermelon tomato

print()
date_info = {'year': "2020", 'month': "01", 'day': "01"}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)
# '2020-01-01.txt'

print()
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
numbers = [2, 1, 3, 4, 7]
print(*numbers, *fruits)
# 2 1 3 4 7 lemon pear watermelon tomato

print()
""" При определении функции можно использовать * ,
    чтобы собрать переменное количество позиционных аргументов,
    переданных в функцию. Они помещаются в кортеж:"""


def roll(*dice):
    print(dice)
    return sum(die for die in dice)


# Эта функция принимает любое количество аргументов:
print(roll(5))
print(roll(5, 10, 6))
print(roll(5, 10, 6, 13))
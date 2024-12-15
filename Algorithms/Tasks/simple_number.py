"""Проверка на простое число, т.е. делиться только на себя и на 1"""
for i in range(5):
    num = int(input('Enter: '))
    k = 0
    for j in range(2, num//2 + 1):
        if num % j == 0:
            k += 1
    if k > 0:
        print("Число не простое!")
    else:
        print("Число простое!")


amount = int(input("Введите кол-во чисел: "))
count = 0
for item in range(amount):
    number = int(input('Введите число: '))
    k = 0
    for i in range(2, number//2 + 1):
        if number % i == 0:
            k += 1
    if k == 0:
        count += 1

print("Количество простых чисел в последовательности:", count)
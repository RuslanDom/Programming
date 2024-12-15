
def factor_number(number):
    factorial = 1
    total = 0
    for i in range(1, number + 1):
        factorial *= i
        total += factorial

    return total, factorial

num = int(input("Введите число: "))
result = factor_number(num)

print(f'Факториал числа: {num} равен = {result[1]}, а сумма равна {result[0]}')





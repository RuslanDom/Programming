# Вводится число N,
# далее еще N − 1 чисел:
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.



# Номер пропавшей карточки: 2
N = int(input("Введите количество карточек: "))
summa_cart = 0
for num_cart in range(1, N+1):
    summa_cart += num_cart
for _ in range(1, N):
    while True:
        loss_cart = int(input("Введите номер оставшейся карточки: "))
        if loss_cart < 1 or loss_cart > N:
            print("Такой карточки нет!")
        else:
            break
    summa_cart -= loss_cart
print("Номер пропавшей карточки:", summa_cart)
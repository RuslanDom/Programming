# for i in range(3):
#     print(i)
# for a in range(2,12,2): первое число в параметре начальное значение, конечное значение и шаг
#     print(a)

"""(number % 10) - получает последнию цифру числа
   (number // 10) - получает число без последней цифры"""
num = int(input('Enter number: '))
summa = 0
while num != 0:
    last_num = num % 10
    if last_num == 5:
        print("Разрыв")
        break
    summa += last_num
    num //= 10
print("Сумма =", summa)



word = 'Ruslan'
for i in word:
    if i == "s":
        print(i)
word = 'Megamarket'
numb = 0
for x in word:
    if x == "a":
        numb += 1
print("Буква повторяется ",numb, " раза.")


z = 10
while z<=20:
    print(z)
    z+=2

bool = True
num = 1
while bool:
    print("Совершенна итерация номер: ", num)
    num+=1
    stop = input('Введите код остановки цикла: ')
    if stop == "111":
        print("Вы отключили бесконечный цикл!")
        bool = False

number = 10
for el in range(20):
    el += 1
    if el % 2 == 0: # A % B ==0 деление на 2 без остатка
        continue
    else:
        print(el)



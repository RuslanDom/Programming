print(10, "String", 11, sep='---', end="&\n")  # sep разделяет данные
print("Second line", end='')
print(10*5)
print(2**3)
print(5/3)
print(5//3)  # // округляет до целого числа к меньшему
print(min(5, 23, 6, 74, 12))  # находит минимальное число
print(max(5, 23, 6, 74, 12))
print(abs(-10))  # передаёт число по модулю
print(pow(5, 2))  # возводит в степень как **
print(round(10/3))  # округляет к близжайшему

# number = input("Введите число: ")
# print(number)
# del number # удаляет переменную
# print(number)
num = 25
digit = 4.5  # float
word = "Слово"  # string
ok = True  # bool
no_ok = False
no_word = "10"
print(no_ok,word)
# print(ok + word) нельзя сложить bool и string
print(str(digit) + word)  # str приводит к строке
print(int(no_word) + num)

print(word*3, word*2, sep="$$$")




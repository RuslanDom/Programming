# if elif else условные операторы

num = int(input("Введите число до 10: "))
if num == 5 and num>0:
    print("yes")
elif num<0 or num == 0:
    print("not right num")
else:
    print("no")

isHappy = True
if isHappy:# Проверяет на == True
    print("That`s right")
if not isHappy:# if not Проверяет на == False
    print("Not right")

data = input("Введите да или нет ")

number = 5 if data=="да" else 0 # Тернарный оператор, уменьшает код
print(number)

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

#Сначала записывается результат, затем условие и в конце второй вариант результата
res = print("ok") if num_1 == num_2 else print("bad")

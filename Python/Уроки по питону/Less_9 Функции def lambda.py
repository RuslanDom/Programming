def func(a,b,c):
    #pass - аналог ничего, функция не сработает
    return a + b + c

num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
num3 = int(input("Введите число: "))
summa = func(num1,num2,num3)
print('Result: ',summa)

# Анонимные функции
stepen = lambda a,b: a**b
result = stepen(int(input("Enter numb 1: ")),int(input("Enter numb 2: ")))
print(result)
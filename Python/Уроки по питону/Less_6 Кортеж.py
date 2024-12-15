# В кортеже (tuple) как и в списках храняться данные, они занимают меньше памяти
# В кортеже нельзя менять значения данных

data = (2,5,7,12,5,33,"Строчка кода")

print(data[0::2])
print(data.count(5))
print(len(data))

#Создание кортежа(tuple)

data_1 = 2, 22, 11, True

print(data_1)

#Перебор кортежа двумя разными циклами
for i in data:
    print(i)

el = 0
while el < len(data):
    print(data[el])
    el += 1

#Переобразовать список в кортеж

nums = [1,3,5,7,9]
string = "HelloWorld"

nums = tuple(nums)
string = tuple(string)

print(nums)
print(string)
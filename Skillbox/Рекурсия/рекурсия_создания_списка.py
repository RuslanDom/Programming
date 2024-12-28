num = int(input('Введите число: '))
list_ = []
def rec_func(num):
    if num == 0:
        return 0
    r = rec_func(num - 1) + 1
    list_.append(r)
    return r

rec_func(num)
print(list_)

def counter(num):
    if num < 1:
        return 1
    return counter(num - 1), print(num)


number = int(input("Введите число: "))
counter(number)








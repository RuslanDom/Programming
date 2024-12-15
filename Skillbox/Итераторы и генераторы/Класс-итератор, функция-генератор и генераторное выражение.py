
chose_number = int(input('Введите число: '))
# First method
result_1 = (i_num ** 2 for i_num in range(1, chose_number))
print('Генераторное выражение:')
for i_num in result_1:
    print(i_num)


# Second method
class Iter:
    def __init__(self, number: int):
        self.__number = number
        self.__count = 0

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self) -> int:
        self.__count += 1
        if self.__count < self.__number:
            return self.__number ** 2
        else:
            raise StopIteration


result_2 = Iter(chose_number)
print('Класс-итератор:')
for i_num in result_2:
    print(i_num)


# Third method
def my_generator(number: int):
    for i_number in range(1, number):
        yield i_number


result_3 = my_generator(chose_number)
print("Функция генератор:")
for i_num in result_3:
    print(i_num)
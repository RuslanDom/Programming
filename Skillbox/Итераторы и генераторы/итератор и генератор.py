"""class Iter:
    def __init__(self, stop):
        self.__counter = 0
        self.__stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.__stop <= self.__counter:
            raise StopIteration
        else:
            self.__counter += 1
            return self.__counter - 1


my_iter = Iter(500)
for i_el in my_iter:
    print(i_el)"""

"""from random import random


class Iter:
    def __init__(self, stop_num):
        self.__stop_num = stop_num
        self.__counter = 0
        self.__number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__stop_num > self.__counter:
            self.__counter += 1
            x = round(random(), 2)
            self.__number += x
            return self.__number
        else:
            raise StopIteration


my_iter = Iter(10)
for i_elem in my_iter:
    print(i_elem)"""


class Primes:
    def __init__(self, N):
        self.__N = N
        self.__counter = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter <= self.__N:
            is_flag = True
            for num in range(2, self.__counter):
                if self.__counter % num == 0:
                    is_flag = False
            if is_flag:
                return self.__counter

        else:
            raise StopIteration


pr = Primes(50)
print(pr)
# for i in pr:
#     print(i)

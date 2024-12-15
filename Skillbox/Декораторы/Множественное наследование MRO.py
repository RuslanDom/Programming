from typing import List


class Person:
    """Базовый класс человек"""

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def shout(self):
        print('Я - Человек')


class Employee(Person):
    """Работник. Дочерний класс от Person"""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__salary = 20000

    def get_salary(self) -> int:
        return self.__salary

    def shout(self):
        print('Я - Работник')


class Parent(Person):
    """Родитель. Дочерний класс Person"""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__kids = ['Tom', 'Bob']

    def get_kids(self) -> List[str]:
        return self.__kids

    def shout(self):
        print('Я - Родитель')


class Citizen(Parent, Employee):
    """Житель. Является и родителем и работником"""

    def shout(self):
        print('Я - Житель')


my_citizen = Citizen(name='Anton', age=30)
print(my_citizen.get_salary())
print(my_citizen.get_kids())
my_citizen.shout()

""" MRO - Method Resolution Order для решение Diamond problem"""
""" 1 - Citizen
    2 - Parent
    3 - Employee
    4 - Person
    Сначало выполняется метод из класса наследника, затем родительские слева на право как определены (Parent, Employee) 
    и в конце super класс Person
    Метод __init__ тоже работает через MRO и запросы выглядят так
    Paren.__init__ -> Employee.__init__ -> Person.__init__ 
"""
# Получить порядок MRO можно  так:
print(my_citizen.__class__.__mro__)

from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный базовый класс фигура

    Args and attrs:
        pos_x (int): координата x
        pos_y (int): координата y
        length (int): длина фигуры
        width (int): ширина фигуры
    """
    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    """  Абстрактный метод. Отличие в том, что теперь невозможно создать инстанс этого класса - Figure(1, 1, 1, 1)"""
    @abstractmethod
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


""" Класс типа Mixin позволяет добавлять функционал классам не изменяя их и исключая конфликты
    Если бы метод resize() был бы прописан внутри родительского класса Figure, тогда возникла бы ошибка
    при создании экземрляра класса Square, так как ему передаётся 3 аргумента, а не 4 (width - отсутствует)"""


class ResizableMixin:
    def resize(self, length: int, width: int) -> None:
        self.length = length
        self.width = width


class Rectangle(Figure, ResizableMixin):
    """ Прямоугольник. Родительский класс Figure"""
    pass


class Square(Figure, ResizableMixin):
    """ Квадрат. Родительский класс Figure"""
    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)


rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
square_1 = Square(pos_x=50, pos_y=70, size=7)

for figure in [rect_1, rect_2, square_1]:
    new_size_x = figure.length * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)

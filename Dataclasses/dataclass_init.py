"""1. Упрощенное создание пользовательских типов данных
Модуль dataclasses предоставляет декоратор и функции для автоматического добавления сгенерированных специальных методов,
таких как __init__() и __repr__(), в определяемые пользователем классы.
Атрибуты класса - переменные для использования в этих сгенерированных методах определяются с использованием аннотаций типов."""

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    price: float
    count: int = 1

    def total_cost(self):
        return self.price * self.count

# Декоратор @dataclass помимо прочего, добавит метод __init__(), который выглядел бы так:
    """
    def __init__(self, title: str, price: float, count: int=0):
        self.title = title
        self.price = price
        self.count = count
    """
# Пример
b = Book("jungle", 500, 10)
print("Book -", b.title, ":", b.total_cost(), "price all books")

"""2. Обработка после инициализации, метод __post_init__()"""
# Позволяет инициализировать значения полей, которые зависят от одного или нескольких других полей
from dataclasses import field

@dataclass
class MyType:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b

# >>> mytype = MyType(7, 9)
# >>> mytype
# MyType(a=7, b=9, c=16)

# >>> n = NewType(10, 5)
# >>> n
# NewType(a=10, b=5, c=15)

"""3. Поле dataclass как переменная ClassVar."""
# Если поле типизировано typing.ClassVar,
# то оно исключается из рассмотрения как поле и игнорируется механизмами класса данных.

from typing import ClassVar

@dataclass
class MyNewType:
    x: int
    y:int
    n: ClassVar

# >>> mytype = MyNewType(7, 9)
# >>> mytype
# MyType(x=7, y=9)

# присвоим переменной класса данных `n` значение
# >>> mytype.n = 5
# переменная `n` игнорируется механизмами
# класса данных и не будет видна как поле
# >>> mytype
# Point(x=7, y=9)

# хотя со значением `n` можно работать
# >>> mytype.n
# 5

"""4. Поле dataclass только для инициализации InitVar"""
# Он делает это, проверяя, имеет ли тип поля тип dataclasses.InitVar.
# Если поле является InitVar, то оно считается псевдополем, которое называется полем только для инициализации.
# Поскольку это не истинное поле, оно не возвращается функцией fields() уровня модуля.
from dataclasses import InitVar


@dataclass
class MyInitType:
    i: int
    j: int = None
    data_for_init: InitVar[int] = None

    def __post_init__(self, data_for_init):
        if self.j is None and data_for_init is not None:
            self.j = data_for_init + 10

myinittype = MyInitType(1, data_for_init=2)

"""4. Неизменяемые классы данных dataclass."""
# Невозможно создать действительно неизменяемые объекты Python, но, передав Frozen=True декоратору dataclasses.dataclass(),
# можно эмулировать неизменяемость. В этом случае классы данных добавят к классу методы __setattr__() и __delattr__().
# При вызове эти методы вызывают ошибку dataclasses.FrozenInstanceError.
# При использовании аргумента frozen=True наблюдается небольшое снижение производительности: __init__() не может
# использовать простое присваивание для инициализации полей и должен использовать object.__setattr__().


from typing import List, Any

@dataclass(frozen=True)
class MyFrozenType:
    x: List[Any]
    y: int


# >>> mytype = MyFrozenType(7, 9)
# >>> mytype
# MyFrozenType(x=[1, 2] y=2)
# >>> mytype.x.append(3)
# >>> mytype.x
# [1, 2, 3]
# --- *** ---
# >>> mytype.y = 15
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 4, in __setattr__
# dataclasses.FrozenInstanceError: cannot assign to field 'x'

"""5. Сравнение Data Classes"""
# Представьте, что вы хотите создать DataClass, представляющий Vector и сравнить их. Как это сделать?
# Для сравнения нужны методы __lt__ или __gt__.
# По умолчанию значение параметра order в Data Class равняется False.
# Если поменять его на True, то методы __lt__, __le__, __gt__ и __ge__ для Data Class будут сгенерированы автоматически.
# Таким образом можно сравнить объекты так, будто бы они являются кортежами полей.
# Разберем на примере. Задав order значение True, можно сравнить v2 и v1. Но есть проблема логики сравнения.
# Если сравнить, например, v2 > v1, то векторы будут сравниваться вот так: (8, 15) > (7, 20).
# Таким образом значением операции будет True.
# --- *** ---
# |- Стоит напомнить, что сравнение кортежей происходит по порядку. Сначала сравниваются 8 и 7, и если результат равен True,
# |- то результатом всего сравнения будет True. Если бы они были равны, то произошло бы сравнение 15 > 20 и результат стал бы False.
# --- *** ---

@dataclass(order=True)
class Vector:
    x: int
    y: int
    magnitude: int = field(init=False)

    def __post_init__(self):
        self.magnitude = abs(self.x - self.y)


v1 = Vector(8, 15)
v2 = Vector(7, 20)
print(v1 > v2) # True
print(v2 > v1) # False
# Очевидно, что в таком сравнении нет никакого смысла. Правильнее было бы сравнивать величину векторов.
# Проблема в том, что не хотелось бы высчитывать эту величину самостоятельно при создании экземпляров.

# >>> v1.magnitude > v2.magnitude
# False
# >>> v1.magnitude < v2.magnitude
# True

"""6. Значения по умолчанию для полей"""

@dataclass
class CircleArea:
    r: int
    pi: float = 3.14

    @property
    def area(self):
        return self.pi * (self.r ** 2)

a = CircleArea(2)
print(repr(a))  # вернется: CircleArea(r=2, pi=3.14)
print(a.area)  # вернется: 12.56

"""7. Конвертация в словарь или кортеж"""
# Можно получить атрибуты Data Class в кортеже или словаре.
# Для этого нужно лишь импортировать функции asdict и astuple из Data Class.

from dataclasses import asdict, astuple


@dataclass
class Vector_as:
    x: int
    y: int
    z: int


v = Vector_as(4, 5, 7)
print(asdict(v))  # Вернется: {'x': 4, 'y': 5, 'z': 7}
print(astuple(v))  # Вернется: (4, 5, 7)

"""8. Наследование"""
# Можно создавать подклассы для Data Class как для обычных классов в Python.

@dataclass
class Employee:
    name: str
    lang: str


@dataclass
class Developer(Employee):
    salary: int


Alex = Developer('Alex', 'Python', 5000)
print(Alex)  # Вернется: Developer(name='Alex', lang='Python', salary=5000)

# Но есть распространенная ошибка при использовании наследования.
# Когда к примеру значением поля lang по умолчанию является Python,
# нужно задавать значения по умолчанию и для всех остальных полей идущих за lang.

"""
@dataclass
class Employee:
    name: str
    lang: str = 'Python'      lang - имеет значение по умолчанию


@dataclass
class Developer(Employee):
    salary: int = 0           значит и salary должно иметь значение по умолчанию
    """






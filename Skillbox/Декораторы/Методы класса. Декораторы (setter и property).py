class Person:
    """
    Человек

    Args:
        name(str): Имя
        age(int): Возраст

    Attributes:
        _name(str): Имя
        _age(int): Возраст (от 1 до 100, иначе ошибка)
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Имя человек: {self.name}\nВозраст: {self.age}'

    @property
    def age(self):
        """ Геттер возращает возраст"""
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """
            Сеттер.
            Устанавливает возраст в диапазоне от 1 до 100,
            иначе выбрасывает исключение
        """
        if age in range(1, 100):
            self._age = age
        else:
            raise Exception("Недопустимый возраст")

    @property
    def name(self):
        """ Геттер возращает имя"""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


tom = Person('Tom', 25)
print(tom)
print(tom.age)
tom._age = 33
print(tom.age)
print(tom)


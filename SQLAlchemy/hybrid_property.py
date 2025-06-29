from sqlalchemy import Column, Integer, func
from sqlalchemy.orm import Session, aliased, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

Base = declarative_base()

"""
Расширение hybrid предоставляет специальную форму декоратора методов, занимает около 50 строк кода и 
практически не зависит от остальной части SQLAlchemy. Теоретически оно может работать с любой системой выражений
на основе дескрипторов.
Рассмотрим отображение Interval, представляющее целое число start и end значения. Мы можем определить функции более 
высокого уровня на отображенных классах, которые производят выражения SQL на уровне класса и оценку выражений Python 
на уровне экземпляра. Ниже каждая функция, декорированная hybrid_method или, 
hybrid_property может получить self как экземпляр класса или как сам класс:
"""

class Interval(Base):
    __tablename__ = 'interval'

    id = Column(Integer, primary_key=True)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @hybrid_property
    def length(self):
        return self.end - self.start

    @hybrid_method
    def contains(self, point):
        return (self.start <= point) & (point <= self.end)

    @hybrid_method
    def intersects(self, other):
        return self.contains(other.start) | self.contains(other.end)

    @hybrid_property
    def radius(self):
        return abs(self.length) / 2

    @radius.expression
    def radius(cls):
        return func.abs(cls.length) / 2

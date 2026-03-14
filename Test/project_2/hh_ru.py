x = 60
print(x)
print(bin(x))

print(~x)
print(bin(~x))


print((1 or 2) + ~1)  # -1

a = 10
b = 5
# print(a = b) # Допущена ошибка

d = {1: "one", 3: "three", 2: "two", "4": "four"}
d.pop("4")
d.setdefault(5, "five")
# d.sorted() # Словарь не сортируется sorted

def score(cf, *scores):
    for i in scores:
        print(cf * i)

cf = 0.2
scoress = [4, 5, 4]
score(cf, *scoress)

import re

str_ = "3 products for 200.99"
ptr = r"\d+.\d"
match = re.search(ptr, str_)
print(match.group()) # 200.9


from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def move(self):
        pass

class Queen(Piece):
    def move(self):
        print("Queen step")


# a = Piece() Нельзя создать абстрактный класс
b = Queen()
# a.move()  Абстрактный метод нельзя вызвать
b.move()


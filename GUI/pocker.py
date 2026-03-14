import random
from typing import List

num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
mast = ['Буби', 'Крести', 'Черви', 'Пики']

class Cart:
    def __init__(self, num, mast) -> None:
        self.coloda = []
        self.num = num
        self.masts = mast
    
    def create_coloda(self):
        while len(self.coloda) < 52:
            self.number = random.choice(self.num)
            self.mast = random.choice(self.masts)
            cart = self.number + " " + self.mast
            if cart not in self.coloda:
                self.coloda.append(cart)
            else:
                continue
        return self.coloda

c = Cart(num=num, mast=mast)

# print(coloda)


def my_steck(coloda):
    my = []
    cart1 = random.choice(coloda)
    coloda.remove(cart1)
    cart2 = random.choice(coloda)
    coloda.remove(cart2)
    print("---" * 30)
    my.append(cart1)
    my.append(cart2)
    print(my)
    return my
    

def com_steck(coloda):
    com = []
    cart1 = random.choice(coloda)
    coloda.remove(cart1)
    cart2 = random.choice(coloda)
    coloda.remove(cart2)
    com.append(cart1)
    com.append(cart2)
    return com



def first_blend(coloda):
    stack = []
    cart1 = random.choice(coloda)
    coloda.remove(cart1)
    cart2 = random.choice(coloda)
    coloda.remove(cart2)
    cart3 = random.choice(coloda)
    coloda.remove(cart3)
    stack.append(cart1)
    stack.append(cart2)
    stack.append(cart3)
    return stack

def next_blend(coloda):
    cart1 = random.choice(coloda)
    coloda.remove(cart1)
    return cart1

def check_combinations(first: List, second: List):
    

    return



while True:
    coloda = c.create_coloda()
    cash = 0

    I = my_steck(coloda=coloda)
    YOU = com_steck(coloda=coloda)
    cash += int(input('Сделай ставку: '))

    f = first_blend(coloda=coloda)
    I.extend(f)
    YOU.extend(f)
    print(I)
    cash += int(input('Сделай ставку: '))

    print("---" * 30)
    n = next_blend(coloda=coloda)
    I.append(n)
    YOU.append(n)
    print(I)
    cash += int(input('Сделай ставку: '))

    print("---" * 30)
    n = next_blend(coloda=coloda)
    I.append(n)
    YOU.append(n)
    print(I)
    cash += int(input('Сделай крайнюю ставку: '))
    print(YOU)
    print(f"Банк в {cash}$ забирает победитель!")
    break

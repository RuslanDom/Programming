import tkinter as tk
"""shuffle рандомно перемешивает изменяемые элементы к примеру list(список)"""
from random import shuffle
class MyButton(tk.Button):
    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, font="Arial 15 bold", width=3, *args, **kwargs)
        self.x = x
        self.y = y
        self.is_bomb = False
        self.number = number
class Game:
    win = tk.Tk()
    row = 10
    column = 10
    MINES = 35
    def __init__(self):
        self.buttons = []
        count = 1
        for i in range(Game.row):
            temp = []
            for j in range(Game.column):
                but = MyButton(Game.win, x=i, y=j, number=count)
                temp.append(but)
                count += 1
            self.buttons.append(temp)

    def draw(self):
        for i in range(Game.row):
            for j in range(Game.column):
                self.buttons[i][j].grid(row=i, column=j)

    def start(self):
        Game().draw()                   # Можно записать вот так  -  self.draw()
        Game().insert_mines()           # Аналогично  -  self.insert_mines()
        Game.win.mainloop()
    @staticmethod
    def get_mines_places():
        index_mines = list(range(1, Game.row * Game.column + 1))    # Список от 1 до количества всех кнопок +1 по порядку
        shuffle(index_mines)                                        # Перемешиваем созданный список
        return index_mines[:Game.MINES]         # Берём индексы ячеек из перемешанного списка от начала срез (:) до кол.ва мин (Game.MINES)

    def insert_mines(self):
        inx_mine = self.get_mines_places()
        for row in self.buttons:
            for but in row:
                if but.number in inx_mine:
                    but.is_bomb = True




gg = Game()
gg.start()






























# import tkinter as tk
#
# class Game:
#     win = tk.Tk()
#     row = 10
#     column = 10
#
#     def __init__(self):
#         self.button = []
#         for i in range(Game.row):
#             pole = []
#             for j in range(Game.column):
#                 but = tk.Button(Game.win, width=3, font="Calibri 15 bold")
#                 pole.append(but)
#             self.button.append(pole)
#
#     def draw(self):
#         for i in range(Game.row):
#             for j in range(Game.column):
#                 self.button[i][j].grid(row=i, column=j)
#
#     def start(self):
#         Game().draw()
#         Game.win.mainloop()
#
# Game().start()
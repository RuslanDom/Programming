import tkinter as tk
from random import shuffle
colors = {
    1: "blue",
    2: "red",
    3: "green",
    4: "yellow",
    5: "orange",
    6: "purple",
    7: "brown",
    8: "grey"
}
class MyBut(tk.Button):
    def __init__(self, master, num=0):
        super(MyBut, self).__init__(master, font='Calibri 20 bold', width=3, relief=tk.RAISED, bd=5)
        self.is_mine = False
        self.num = num
        self.count = 0
    def __repr__(self):
        if self.is_mine == True:
            self.count = 'b'
        return f'{self.count}'
class Game:
    win = tk.Tk()
    row = 10
    column = 10
    Mines = 10
    def __init__(self):
        self.button = []
        for i in range(0, self.row + 2):
            temp = []
            for j in range(0, self.column + 2):
                btn = MyBut(self.win)
                btn.config(command=lambda but=btn: self.press_but(but))
                temp.append(btn)
            self.button.append(temp)


    def press_but(self, but: MyBut):
        if but.is_mine:
            but.config(text='*', bg='red')
        elif but.count in colors:
            but.config(text=but.count, fg=colors[but.count])
        else:
            but.config(relief=tk.SUNKEN)
        but.config(relief=tk.SUNKEN)

    def draw(self):
        for i in range(1, self.row + 1):
            for j in range(1, self.column + 1):
                btn = self.button[i][j]
                btn.grid(row=i, column=j)

    def print(self):
        for i in range(1, self.row + 1):
            for j in range(1, self.column + 1):
                btn = self.button[i][j]
                print(f'{btn.__repr__()}', end=' ')
            print()


    def start(self):
        self.draw()
        self.get_mines()
        self.find_neighbors()
        self.print()
        self.win.mainloop()


    @classmethod
    def get_mine_inx(cls):
        list_mine = list(range(0, cls.row * cls.column + 1))
        shuffle(list_mine)
        return list_mine[:cls.Mines]
    def get_mines(self):
        inx_list_mines = self.get_mine_inx()
        amount = 0
        for i in range(1, self.row + 1):
            for j in range(1, self.column + 1):
                btn = self.button[i][j]
                amount += 1
                btn.num = amount
                if btn.num in inx_list_mines:
                    btn.is_mine = True

    def find_neighbors(self):

        for i in range(1, self.row + 1):
            for j in range(1, self.column + 1):
                btn = self.button[i][j]
                neighbour = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            but = self.button[i+row_dx][j+col_dx]
                            if but.is_mine:
                                neighbour += 1
                btn.count = neighbour

game = Game()
game.start()
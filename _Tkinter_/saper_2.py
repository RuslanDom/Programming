import tkinter as tk
from random import shuffle

colors = {
    1: 'blue',
    2: 'green',
    3: 'red',
    4: 'purple',
    5: 'light green',
    6: 'yellow',
    7: 'orange',
    8: 'pink'
}


class MyButton(tk.Button):
    def __init__(self, master, x, y, num=0):
        super(MyButton, self).__init__(master, width=3, font="Calibri 15 bold", relief="raised", bd=5, bg="#B5B5B5")
        self.x = x
        self.y = y
        self.num = num
        self.is_mine = False
        self.count_bomb = 0


    def __repr__(self):
        return f'But: {self.num} Mine: {self.is_mine}'


class Game:
    window = tk.Tk()
    ROW = 10
    COLUMN = 10
    MINES = 10
    window.title('S_A_P_E_R')

    def __init__(self):
        self.buttons = []

        for i in range(self.ROW + 2):
            col = []
            for j in range(self.COLUMN + 2):
                btn = MyButton(self.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                col.append(btn)

            self.buttons.append(col)

    @staticmethod
    def click(clicked_button: MyButton):
        if clicked_button.is_mine:
            clicked_button.config(text='*', disabledforeground='black', bg='red')
        elif clicked_button.count_bomb in colors:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground=colors[clicked_button.count_bomb], bg="#D1D1D1")
        else:
            clicked_button.config(bg="#D1D1D1")

        clicked_button.config(state="disabled", relief="sunken")

    def draw(self):
        for i in range(1, self.ROW + 1):
            for j in range(1, self.COLUMN + 1):
                self.buttons[i][j].grid(row=i, column=j)

    def print(self):
        for btn in self.buttons:
            print(btn)

    # def open_but(self):
    #     for i in range(1, self.ROW + 1):
    #         for j in range(1, self.COLUMN + 1):
    #             btn = self.buttons[i][j]
    #             if btn.count_bomb == 0:
    #                 for row_dx in [-1, 0, 1]:
    #                     for col_dx in [-1, 0, 1]:
    #                         btn = self.buttons[i+row_dx][j+col_dx]
    #                         btn.config(state="disabled", relief="sunken", bg="#D1D1D1")
    #                         print('HHHHHHHHHHHHHHHHHHHHHHHHHH')


    def start(self):
        self.draw()
        self.__get_mine()

        self.count_mines_in_ceil()
        # self.open_but()
        # self.print()
        self.window.mainloop()

    @classmethod
    def __get_inx(cls):
        list_num = list(range(1, cls.ROW * cls.COLUMN + 1))
        shuffle(list_num)
        return list_num[:cls.MINES]

    def __get_mine(self):
        index = self.__get_inx()
        number = 1
        for i in range(1, self.ROW + 1):
            for j in range(1, self.COLUMN + 1):
                btn = self.buttons[i][j]
                btn.num = number
                number += 1
                if btn.num in index:
                    btn.is_mine = True

    def count_mines_in_ceil(self):
        for i in range(1, self.ROW + 1):
            for j in range(1, self.COLUMN + 1):
                btn = self.buttons[i][j]
                count_nearby = 0
                if not self.buttons[i][j].is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i + row_dx][j + col_dx]
                            if neighbour.is_mine:
                                count_nearby += 1

                btn.count_bomb = count_nearby


game = Game()
game.start()

import tkinter as tk
from random import shuffle
colors = {
    1: 'blue',
    2: '#008200',
    3: '#FF0000',
    4: '#000084',
    5: '#840000',
    6: '#008284',
    7: '#840084',
    8: '#000000'
}

class My_button(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(My_button, self).__init__(master, width=3, font='Calibri 15 bold')
        self.number = number
        self.x = x
        self.y = y
        self.is_Mine = False
        self.count_bomb = 0

    def __repr__(self):
        return f'My_button ({self.x} {self.y}) №{self.number} {self.is_Mine}'


class Minesweeper:

    window = tk.Tk()
    ROW = 10
    COLUMN = 10
    Mines = 10

    def __init__(self):

        self.buttons = []
        for i_row in range(self.ROW + 2):
            tmp_list = []
            for i_col in range(self.COLUMN + 2):
                btn = My_button(master=self.window, x=i_row, y=i_col)
                btn.config(command=lambda button=btn: self.click(button))
                tmp_list.append(btn)

            self.buttons.append(tmp_list)

    def click(self, clicked_button: My_button):
        print(clicked_button)
        color = colors.get(clicked_button.count_bomb, 'white')
        if clicked_button.is_Mine:
            clicked_button.config(text='*', bg='red', disabledforeground='black')
        else:

            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
            else:
                clicked_button.config(text='', disabledforeground=color)
        clicked_button.config(state='disabled', fg=color, relief=tk.SUNKEN, bd=2)

    def create_widgets(self):
        for i_row in range(1, self.ROW + 1):
            for i_col in range(1, self.COLUMN + 1):
                btn = self.buttons[i_row][i_col]
                btn.grid(row=i_row, column=i_col)

    def OPEN_ALL_BUTTONS(self):
        for i_row in range(1, self.ROW + 1):
            for i_col in range(1, self.COLUMN + 1):
                btn = self.buttons[i_row][i_col]
                if btn.is_Mine:
                    btn.config(text='*', bg='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'white')
                    btn.config(text=btn.count_bomb, fg=color)



    def print_buttons(self):
        for i_row in range(1, self.ROW + 1):
            for i_col in range(1, self.COLUMN + 1):
                btn = self.buttons[i_row][i_col]
                if btn.is_Mine:
                    print('B', end=' ')
                else:
                    print(btn.count_bomb, end=' ')
            print()

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        # self.OPEN_ALL_BUTTONS()
        self.print_buttons()
        self.window.mainloop()

    def insert_mines(self):
        insert_mine = self.get_mines_places()
        count = 1
        for i_row in range(1, self.ROW + 1):
            for i_col in range(1, self.COLUMN + 1):
                btn = self.buttons[i_row][i_col]
                btn.number = count
                if btn.number in insert_mine:
                    btn.is_Mine = True
                count += 1

    def count_mines_in_buttons(self):
        for i_row in range(1, self.ROW + 1):
            for i_col in range(1, self.COLUMN + 1):
                btn = self.buttons[i_row][i_col]
                count_bomb = 0
                if not btn.is_Mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i_row + row_dx][i_col + col_dx]
                            if neighbour.is_Mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb
    def get_mines_places(self):
        indexes = list(range(self.ROW * self.COLUMN + 1))
        shuffle(indexes)
        return indexes[:self.Mines]


game = Minesweeper()
game.start()




import tkinter as tk
from random import randint



win = tk.Tk()
win.geometry('400x600')
win.title('CheckButton-Radio and ComboBox')
text = tk.BooleanVar()
text.set(False)


def that_is_all():
    lis = [check, check_2, check_3]
    for l in lis:
        l.select()
def change():
    lis = [check, check_2, check_3]
    for l in lis:
        l.toggle()
def info():
    print(text.get())
    lis = [check, check_2, check_3]
    for l in lis:
        color = ['red', 'green', 'yellow', 'blue', 'white', 'brown']
        i = randint(0, 5)
        l.config(bg=color[i])

check = tk.Checkbutton(win, text='You ready?', indicatoron=False, variable=text, onvalue=True, offvalue=False)
check.pack()

check_2 = tk.Checkbutton(win, text="Are you a male?")
check_2.pack()

check_3 = tk.Checkbutton(win, text="Are you a female?")
check_3.pack()

but_all = tk.Button(win, text="ALL", command=that_is_all).pack()
but_switch = tk.Button(win, text="CHANGE", command=change).pack()
but_inf = tk.Button(win, text='info', command=info).pack()

win.mainloop()


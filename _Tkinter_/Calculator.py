import tkinter as tk

def press_key(event):
    if event.char.isdigit():
        numb(event.char)
    elif event.char in '+-*/':
        operation(event.char)
    elif event.char == '\r':
        result()

win = tk.Tk()
win.geometry('255x310')
win.resizable(False, False)
win.title("Calculator")
win.config(bg='black', pady=5)
win.bind('<Key>', press_key)


def numb(num):
    dis = display.get()
    if dis[0] == '0':
        dis = dis[1:]
    display.delete(0, tk.END)
    display.insert(0, dis + num)
def operation(i):
    dis = display.get()
    if dis[-1] in "+-*/":
        dis = dis[:-1]
    display.delete(0, tk.END)
    display.insert(0, dis + i)
def add_button(num):
    return tk.Button(text=num, relief='raised', bd=5, font=("Arial", 15, 'bold'), command=lambda: numb(num))
def add_operation_but(i):
    return tk.Button(text=i, relief='raised', bd=5, font=("Arial", 15, 'bold'), command=lambda: operation(i))
def add_result_but(num):
    return tk.Button(text=num, relief='raised', bd=5, font=("Arial", 15, 'bold'), command=result)
def result():
    calc = display.get()
    if calc[-1] in '+-*/':
        calc = calc + calc[:-1]
    display.delete(0, 'end')
    try:
        r = round(eval(calc), 10)
        display.insert(0, r)
    except (NameError, SyntaxError):
        calc = calc[:-1]
        display.delete(0, 'end')
        display.insert(0, calc)
def add_del_but(num):
    return tk.Button(text=num, relief='raised', bd=5, font=("Arial", 15, 'bold'), command=lambda: delete())
def delete():
    display.delete(0, 'end')
    display.insert(0, '0')


display = tk.Entry(win, bg='light green', bd=5, width=22, font=("Arial", 15, 'bold'), justify=tk.RIGHT)
display.grid(row=0, column=0,  columnspan=4, stick="wens")
display.insert(0, '0')

add_button("1").grid(row=3, column=0, padx=10, pady=10, stick='wens')
add_button("2").grid(row=3, column=1, padx=10, pady=10, stick='wens')
add_button("3").grid(row=3, column=2, padx=10, pady=10, stick='wens')
add_button("4").grid(row=2, column=0, padx=10, pady=10, stick='wens')
add_button("5").grid(row=2, column=1, padx=10, pady=10, stick='wens')
add_button("6").grid(row=2, column=2, padx=10, pady=10, stick='wens')
add_button("7").grid(row=1, column=0, padx=10, pady=10, stick='wens')
add_button("8").grid(row=1, column=1, padx=10, pady=10, stick='wens')
add_button("9").grid(row=1, column=2, padx=10, pady=10, stick='wens')
add_button("0").grid(row=4, column=0, padx=10, pady=10, stick='wens')

add_del_but("C").grid(row=4, column=1, padx=10, pady=10, stick='wens')
add_result_but("=").grid(row=4, column=2, padx=10, pady=10, stick='wens')
add_operation_but("/").grid(row=4, column=3, padx=10, pady=10, stick='wens')
add_operation_but("+").grid(row=1, column=3, padx=10, pady=10, stick='wens')
add_operation_but("-").grid(row=2, column=3, padx=10, pady=10, stick='wens')
add_operation_but("*").grid(row=3, column=3, padx=10, pady=10, stick='wens')




win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=50)
win.grid_columnconfigure(2, minsize=50)
win.grid_columnconfigure(3, minsize=50)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()

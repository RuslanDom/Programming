import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='image/cloudberry.png')
win.iconphoto(False, photo)
win.geometry('400x600+600+200')
win.title('New file')
win.config(bg='light grey')


def info():
    res = name.get()
    pass_res = pass_word.get().strip()
    print(f"{res}\n{pass_res}")



label_1 = tk.Label(win, text="Name", bg='grey', font=("Arial", 10, 'bold'), pady=10).grid(row=0, column=0, stick='we')
name = tk.Entry(win, bg='light yellow')
name.grid(row=0, column=1, stick='wens')
but_1 = tk.Button(win, text='INFO', command=info, bg='blue', fg='yellow', font=("Arial", 10, 'bold'), relief="raised",
                  bd= 10,padx=20, pady=5, anchor='center', activebackground='red').grid(row=2, column=0, stick='we')


label_2 = tk.Label(win, text='Password', bg='white', font=("Arial", 10, 'bold'), pady=10).grid(row=1, column=0, stick='we')
pass_word = tk.Entry(win, bg='pink', show='*')
pass_word.grid(row=1, column=1, stick="wens")


win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=200)

win.mainloop()
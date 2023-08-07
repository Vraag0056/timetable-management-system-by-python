import os
import tkinter as tk
from tkinter import *
from tkinter import ttk


def run_p():

    if combo1.get() =="CS Department":
        root.destroy()
        os.system('py files\\set_timetable.py')
    else:
            if combo1.get() == "Management Department":
                root.destroy()
                os.system('py files\\set_timetable_m.py')
try:
    root = Tk()
    root.title('Select Department for timetable')
    root.geometry('420x250')
    root.configure(bg="#fff")
    root.resizable(False,False)


    tk.Label(
            root,
            text='Select Department For Adding Batch',
            fg='black', bg='white', font=('Consolas', 12, 'bold')
        ).place(x=60, y=50)

    # Label4
    tk.Label(
        root,
        text='Lecture:',fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=60, y=120)


    op = ["Select option","CS Department","Management Department"]
    combo1 = ttk.Combobox(root, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                              values=op
                              )
    combo1.current(0)
    combo1.place(x=180, y=122)

    B2 = tk.Button(
            root,
            text='Select',
            font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
            command=run_p
        )
    B2.place(x=180,y=160)



    root.mainloop()

except Exception as e:
    pass

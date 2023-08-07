import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')
lec = conn.cursor()
s = f"SELECT lecture from timing"
lec.execute(s)
lec = list(lec)

def create_treeview():
    tree['columns'] = ('one', 'two')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=100, stretch=tk.NO)
    tree.column("two", width=200, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Lecture")
    tree.heading('two', text="Time")

def update_treeview():
    t=''
    for row in tree.get_children():
        tree.delete(row)
    cur = conn.cursor()
    cur.execute("SELECT * FROM timing")
    cur = list(cur)
    for row in cur:
        # print(row[0], row[1], row[2])

        tree.insert(
            "",
            0,
            values=(row[1],row[2])
        )
    tree.place(x=500, y=100)

def update_data(lec_entry,combo1):
    lec = conn.cursor()
    s = f"UPDATE timing SET time = '{lec_entry.get()}' WHERE  lecture= '{combo1.get()}'"
    lec.execute(s)
    lec.execute("commit")
    update_treeview()
    lec_entry.insert(0, '')



def update_t():
    lec = conn.cursor()
    s = f"SELECT time from timing where lecture='{combo1.get()}'"
    lec.execute(s)
    lec = list(lec)
    tk.Label(
        root,
        text='Timing:', fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=60, y=200)
    lec_entry = tk.Entry(
        root,
        font=('Consolas', 15),
        width=15
    )
    lec_entry.place(x=180, y=200)
    lec_entry.insert(0, lec[0][0])

    B2 = tk.Button(
        root,
        text='Update Time',
        font=('Consolas', 12), bg='#57a1f8', fg='white', border=0,
        command=lambda lec_entry=lec_entry,combo1=combo1:update_data(lec_entry,combo1)
    )
    B2.place(x=180, y=250)

root = Tk()
root.title('Add Time')
root.geometry('850x400')
root.configure(bg="#fff")
root.resizable(False,False)

tree = ttk.Treeview(root,height=12)
create_treeview()
update_treeview()

tk.Label(
        root,
        text='List of Timings',
    fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=530, y=50)

    # Label2
tk.Label(
        root,
        text='Update Timing',
        fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=60, y=50)

# Label4
tk.Label(
    root,
    text='Lecture:',fg='black', bg='white',
    font=('Consolas', 15)
).place(x=60, y=120)



combo1 = ttk.Combobox(root, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=lec
                          )
combo1.current(0)
combo1.place(x=180, y=122)

B2 = tk.Button(
        root,
        text='Show',
        font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
        command=update_t
    )
B2.place(x=180,y=160)

Label(root,text='Created By : Divyanshu Jain',bg="#fff").place(x=680,y=375)


root.mainloop()

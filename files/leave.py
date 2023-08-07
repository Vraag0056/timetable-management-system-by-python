import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')
lec = conn.cursor()
s = f"SELECT time from timing"
lec.execute(s)
lec = list(lec)
fac = conn.cursor()
s= f"SELECT faculty_initials from faculty"
fac.execute(s)
fac = list(fac)

def create_treeview():
    tree['columns'] = ('one', 'two','three')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=100, stretch=tk.NO)
    tree.column("two", width=200, stretch=tk.NO)
    tree.column("three", width=200, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Faculty")
    tree.heading('two', text="Day")
    tree.heading('three', text="Time")

def update_treeview():
    t=''
    for row in tree.get_children():
        tree.delete(row)
    cur = conn.cursor()
    cur.execute("SELECT * FROM `leave`")
    cur = list(cur)
    for row in cur:
        # print(row[0], row[1], row[2])

        tree.insert(
            "",
            0,
            values=(row[1],row[2])
        )
    tree.place(x=500, y=100)



def parse_data():
    c1 = str(combo1.get())
    c2=  str(combo2.get())
    c3=str(combo3.get())

    lec1 = conn.cursor()
    s = f"SELECT lecture from timing where time='{c3}'"
    lec1.execute(s)
    lec1 = list(lec1)
    btn_st=500
    btn_ed=500
    if(c2=='Monday'):
        lm=1
        while(lm<9):
            if(str(lec1[0][0])=='lecture'+str(lm)):
                btn_st=lm-1
                btn_ed=0
                break
            else:
                lm=lm+1

    if (c2 == 'Tuesday'):
        lm = 1
        while (lm < 9):
            if (str(lec1[0][0]) == 'lecture' + str(lm)):
                btn_st = lm - 1
                btn_ed = 1
                break
            else:
                lm=lm+1

    if (c2 == 'Wednesday'):
        lm = 1
        while (lm < 9):
            if (str(lec1[0][0]) == 'lecture' + str(lm)):
                btn_st = lm - 1
                btn_ed = 2
                break
            else:
                lm=lm+1

    if (c2 == 'Thursday'):
        lm = 1
        while (lm < 9):
            if (str(lec1[0][0]) == 'lecture' + str(lm)):
                btn_st = lm - 1
                btn_ed = 3
                break
            else:
                lm=lm+1

    if (c2 == 'Friday'):
        lm = 1
        while (lm < 9):
            if (str(lec1[0][0]) == 'lecture' + str(lm)):
                btn_st = lm - 1
                btn_ed = 4
                break
            else:
                lm=lm+1


    cur = conn.cursor()
    cur.execute(f"INSERT INTO `leave`(`fac_name`, `time`, `btn_st`, `btn_ed`) values ('{c1}','{str(lec1[0][0])}','{btn_st}','{btn_ed}')")
    cur.execute("commit")
    update_treeview()






root = Tk()
root.title('Add Time')
root.geometry('1050x400')
root.configure(bg="#fff")
root.resizable(False,False)

tree = ttk.Treeview(root,height=12)
create_treeview()
update_treeview()

tk.Label(
        root,
        text='List of Leaves',
    fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=530, y=50)

    # Label2
tk.Label(
        root,
        text='Leaves',
        fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=60, y=50)




tk.Label(
    root,
    text='Faculty:',fg='black', bg='white',
    font=('Consolas', 15)
).place(x=60, y=120)
combo1 = ttk.Combobox(root, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=fac
                          )
combo1.current(0)
combo1.place(x=180, y=122)


tk.Label(
    root,
    text='Day:',fg='black', bg='white',
    font=('Consolas', 15)
).place(x=60, y=180)
combo2 = ttk.Combobox(root, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=['Monday','Tuesday','Wednesday','Thursday','Friday']
                          )
combo2.current(0)
combo2.place(x=180, y=182)
# Label4
tk.Label(
    root,
    text='Time:',fg='black', bg='white',
    font=('Consolas', 15)
).place(x=60, y=240)
combo3 = ttk.Combobox(root, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=lec
                          )
combo3.current(0)
combo3.place(x=180, y=242)

B2 = tk.Button(
        root,
        text='Update',
        font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
    command=parse_data

    )
B2.place(x=180,y=300)

Label(root,text='Created By : Divyanshu Jain',bg="#fff").place(x=680,y=375)


root.mainloop()

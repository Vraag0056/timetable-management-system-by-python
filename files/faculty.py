import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')


def update_data():
    fac_username.delete(0, tk.END)
    fac_password.delete(0, tk.END)
    fac_name.delete(0, tk.END)
    fac_initials.delete(0, tk.END)
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one subject at a time to update!")
            return

        row = tree.item(tree.selection()[0])['values']
        fac_username.insert(0, row[0])
        fac_password.insert(0, row[1])
        fac_name.insert(0, row[2])
        fac_initials.insert(0, row[3])
        cur = conn.cursor()
        cur.execute(f"DELETE FROM faculty WHERE faculty_username= '{row[0]}'")
        cur.execute("commit")
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return
# remove selected data from databse and treeview
def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        cur = conn.cursor()
        cur.execute(f"DELETE FROM faculty WHERE faculty_username = '{tree.item(i)['values'][0]}'")
        cur.execute("commit")
        tree.delete(i)
        update_treeview()

def create_treeview():
    tree['columns'] = ('one', 'two', 'three','four')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=150, stretch=tk.NO)
    tree.column("two", width=150, stretch=tk.NO)
    tree.column("three", width=200, stretch=tk.NO)
    tree.column("four", width=80, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="username")
    tree.heading('two', text="password")
    tree.heading('three', text="name")
    tree.heading('four', text="initials")






def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    cur = conn.cursor()
    cur.execute("SELECT * FROM faculty")
    cur = list(cur)
    for row in cur:

        tree.insert(
            "",
            0,
            values=(row[1],row[2],row[3],row[4])
        )
    tree.place(x=500, y=100)
# Parse and store data into database and treeview upon clcicking of the add button
def parse_data():
    usename = str(fac_username.get()).upper()
    password = str(fac_password.get())
    name = str(fac_name.get()).upper()
    initials= str(fac_initials.get()).upper()


    if usename == "":
        usename = None
    if password == "":
        password = None
    if name=="":
        name = None
    if initials =="":
        initials=None

    if usename is None or password is None or name is None or initials is None:
        messagebox.showerror("Bad Input", "Please fill up all the fields")
        fac_username.delete(0, tk.END)
        fac_password.delete(0, tk.END)
        fac_name.delete(0, tk.END)
        fac_initials.delete(0, tk.END)
        return

    cur = conn.cursor()
    s= "insert into faculty (faculty_username,faculty_password,faculty_name, faculty_initials) values(%s,%s,%s,%s)"
    b1=(usename,password,name,initials)
    cur.execute(s,b1)
    cur.execute("commit")
    update_treeview()

    fac_username.delete(0, tk.END)
    fac_password.delete(0, tk.END)
    fac_name.delete(0, tk.END)
    fac_initials.delete(0, tk.END)





root = Tk()
root.title('Add Faculty')
root.geometry('1100x450')
root.configure(bg="#fff")
root.resizable(False,False)

style= ttk.Style()
style.theme_use("alt")
tree = ttk.Treeview(root,height=12)
create_treeview()
update_treeview()

tk.Label(
        root,
        text='List of Faculties',
    fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=600, y=50)

    # Label2
tk.Label(
        root,
        text='Add/Update Faculty',
        fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=60, y=50)

# Label4
tk.Label(
    root,
    text='Faculty Username:',fg='black', bg='white',
    font=('Consolas', 15)
).place(x=60, y=120)

# Entry1
fac_username = tk.Entry(
    root,
    font=('Consolas', 15),
    width=20
)
fac_username.place(x=260, y=120)

tk.Label(
        root,
        text='Faculty Password:',fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=60, y=180)

fac_password = tk.Entry(
    root,
    font=('Consolas', 15),
    width=20
)
fac_password.place(x=260, y=180)


tk.Label(
        root,
        text='Faculty Name:',fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=60, y=240)

fac_name = tk.Entry(
    root,
    font=('Consolas', 15),
    width=20
)
fac_name.place(x=260, y=240)

tk.Label(
        root,
        text='Initials:',fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=60, y=300)

fac_initials = tk.Entry(
    root,
    font=('Consolas', 15),
    width=20
)
fac_initials.place(x=260, y=300)


    # Button1
B1 = tk.Button(
        root,
        text='Add Faculty',
        font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
        command=parse_data
    )
B1.place(x=150,y=390)

    # Button2
B2 = tk.Button(
        root,
        text='Update Subject',
        font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
        command=update_data
    )
B2.place(x=410,y=390)

B3 = tk.Button(
    root,
    text='Delete Subject(s)',
    font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
    command=remove_data
)
B3.place(x=650, y=390)
Label(root,text='Created By : Divyanshu Jain',bg="#fff").place(x=890,y=420)
root.mainloop()

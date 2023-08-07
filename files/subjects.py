import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')


def update_data():
    subcode_entry.delete(0, tk.END)
    subname_entry.delete("1.0", tk.END)
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one subject at a time to update!")
            return

        row = tree.item(tree.selection()[0])['values']
        subcode_entry.insert(0, row[0])
        subname_entry.insert("1.0", row[1])
        if row[2][0] == "T":
            R1.select()
        elif row[2][0] == "P":
            R2.select()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM SUBJECTS WHERE subject_code= '{row[0]}'")
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
        cur.execute(f"DELETE FROM SUBJECTS WHERE subject_code = '{tree.item(i)['values'][0]}'")
        cur.execute("commit")
        tree.delete(i)
        update_treeview()

def create_treeview():
    tree['columns'] = ('one', 'two', 'three')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=70, stretch=tk.NO)
    tree.column("two", width=300, stretch=tk.NO)
    tree.column("three", width=60, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Code")
    tree.heading('two', text="Name")
    tree.heading('three', text="Type")






def update_treeview():
    t=''
    for row in tree.get_children():
        tree.delete(row)
    cur = conn.cursor()
    cur.execute("SELECT * FROM subjects")
    cur = list(cur)
    for row in cur:
        # pnt(row[0], row[1], row[2])
        if row[3] == 'T':
            t = 'Theory'
        elif row[3] == 'P':
            t = 'Practical'
        tree.insert(
            "",
            0,
            values=(row[1],row[2],t)
        )
    tree.place(x=500, y=100)
# Parse and store data into database and treeview upon clcicking of the add button
def parse_data():
    subcode = str(subcode_entry.get())
    subname = str(subname_entry.get("1.0", tk.END)).upper().rstrip()
    subtype = str(radio_var.get()).upper()

    if subcode == "":
        subcode = None
    if subname == "":
        subname = None

    if subcode is None or subname is None:
        messagebox.showerror("Bad Input", "Please fill up Subject Code and/or Subject Name!")
        subcode_entry.delete(0, tk.END)
        subname_entry.delete("1.0", tk.END)
        return

    cur = conn.cursor()
    s= "insert into subjects (subject_code,subject_name, subject_type) values(%s,%s,%s)"
    b1=(subcode,subname,subtype)
    cur.execute(s,b1)
    cur.execute("commit")
    update_treeview()

    subcode_entry.delete(0, tk.END)
    subname_entry.delete("1.0", tk.END)




root = Tk()
root.title('Add Subject')
root.geometry('1000x450')
root.configure(bg="#fff")
root.resizable(False,False)

style= ttk.Style()
style.theme_use("alt")
tree = ttk.Treeview(root,height=12)
create_treeview()
update_treeview()

tk.Label(
        root,
        text='List of Subjects',
    fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=600, y=50)

    # Label2
tk.Label(
        root,
        text='Add/Update Subjects',
        fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=100, y=50)

# Label4
tk.Label(
    root,
    text='Subject code:',fg='black', bg='white',
    font=('Consolas', 15)
).place(x=100, y=120)

# Entry1
subcode_entry = tk.Entry(
    root,
    font=('Consolas', 15),
    width=15
)
subcode_entry.place(x=270, y=120)

tk.Label(
        root,
        text='Subject Name:',fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=100, y=200)

    # Text
subname_entry = tk.Text(
        root,
        font=('Consolas', 10),
        width=25,

        height=3,
        wrap=tk.WORD
    )
subname_entry.place(x=270, y=200)

    # Label6
tk.Label(
        root,
        text='Subject Type:',fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=100, y=280)
radio_var = tk.StringVar()

# RadioButton1
R1 = tk.Radiobutton(
    root,
    text='Theory',fg='black', bg='white',
    font=('Consolas', 12),
    variable=radio_var,
    value="T"
)
R1.place(x=270, y=280)
R1.select()

    # RadioButton2
R2 = tk.Radiobutton(
        root,
        text='Practical',fg='black', bg='white',
        font=('Consolas', 12),
        variable=radio_var,
        value="P"
    )
R2.place(x=270, y=310)
R2.select()

    # Button1
B1 = tk.Button(
        root,
        text='Add Subject',
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
Label(root,text='Created By : Divyanshu Jain',bg="#fff").place(x=830,y=420)
root.mainloop()

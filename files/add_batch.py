import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')



def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        cur = conn.cursor()
        cur.execute(f"DELETE FROM batch WHERE batch_name = '{tree.item(i)['values'][0]}'")
        cur.execute("commit")
        tree.delete(i)
        update_treeview()

def create_treeview():
    tree['columns'] = ('one')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=120, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Name")






def update_treeview():
    t=''
    for row in tree.get_children():
        tree.delete(row)
    cur = conn.cursor()
    cur.execute("SELECT * FROM batch")
    cur = list(cur)
    for row in cur:
        # print(row[0], row[1], row[2])

        tree.insert(
            "",
            0,
            values=(row[1])
        )
    tree.place(x=500, y=100)
# Parse and store data into database and treeview upon clcicking of the add button
def parse_data():
    subname = str(subname_entry.get()).upper()

    if subname == "":
        subname = None

    if subname is None:
        messagebox.showerror("Bad Input", "Please fill up Subject Code and/or Subject Name!")
        subname_entry.delete(0, tk.END)
        return

    cur = conn.cursor()
    cur.execute(f"insert into batch (batch_name) values ('{subname}')")
    cur.execute("commit")
    update_treeview()

    subname_entry.delete(0, tk.END)




root = Tk()
root.title('Add Batch - CS Department')
root.geometry('750x450')
root.configure(bg="#fff")
root.resizable(False,False)

style= ttk.Style()
style.theme_use("alt")
'''style.configure("Treeview",
                background="silver",
                foreground="black",
                rowheight=25,
                fieldbackground="silver"
                )
style.map('Treeview',
          background=[('selected','green')]
          )'''
tree = ttk.Treeview(root,height=12)
create_treeview()
update_treeview()

tk.Label(
        root,
        text='List of Batches',
    fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=450, y=50)

    # Label2
tk.Label(
        root,
        text='Add/Update Batch',
        fg='black', bg='white', font=('Consolas', 20, 'bold')
    ).place(x=100, y=50)


tk.Label(
        root,
        text='Batch Name:',fg='black', bg='white',
        font=('Consolas', 15)
    ).place(x=100, y=200)

    # Text
subname_entry = tk.Entry(
    root,
    font=('Consolas', 15),
    width=15
)
subname_entry.place(x=270, y=200)



# RadioButton1


    # Button1
B1 = tk.Button(
        root,
        text='Add Batch',
        font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
        command=parse_data
    )
B1.place(x=300,y=240)


B3 = tk.Button(
    root,
    text='Delete Batch',
    font=('Consolas', 12),bg='#57a1f8',fg='white',border=0,
    command=remove_data
)
B3.place(x=500, y=390)
Label(root,text='Created By : Divyanshu Jain',bg="#fff").place(x=590,y=425)

root.mainloop()

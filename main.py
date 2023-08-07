import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys
import mysql.connector

def check():
    conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')
    if conn.is_connected():
        combo = str(combo1.get())
        if combo == "Student":
           pass

        elif combo == "Faculty":
            pass

        elif combo == "Admin":
            cur = conn.cursor()
            s=f"SELECT username,password from admin"
            cur.execute(s)
            cur = list(cur)
            if(cur[0][0]==user.get() and cur[0][1]==passw.get()):
                root.destroy()
                os.system('py files\\admin.py')
            else:
                messagebox.showerror("Invalid", "Invalid Username or Password")


root = Tk()
root.title('Atterndence Management System--Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='binl\\bit.png')
Label(root,image=img,bg='white').place(x=50,y=90)

frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)


def on_enter(e):
    name = user.get()
    if name == 'Username  ':
        user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username  ')
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username  ')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#####

def on_enter(e):
    passw.delete(0, 'end')


def on_leave(e):
    name=passw.get()
    if name=='':
        passw.insert(0, '                    ')

passw = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11),show="*")
passw.place(x=30,y=150)
passw.insert(0,'                    ')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

def show_password():
    if passw.cget('show')=='*':
       passw.config(show='')


    else:
        passw.config(show='*')

check_button = Checkbutton(frame,width=25,fg='black',border=0,bg="white",text='Show Password',font=('Microsoft YaHei UI Light',9,'bold'),command=show_password)
check_button.place(x=-25,y=185)

combo1 = ttk.Combobox(frame,width=25,font=('Microsoft YaHei UI Light',9),
    values=['Student', 'Faculty', 'Admin']
)
combo1.current(2)
combo1.place(x=25,y=235)

Button(frame,width=39,pady=7,text = 'Sign in',bg='#57a1f8',fg='white',border=0,command=check).place(x=35,y=300)

Label(root,text='Created By : Divyanshu Jain',bg="#fff").place(x=750,y=470)

root.mainloop()

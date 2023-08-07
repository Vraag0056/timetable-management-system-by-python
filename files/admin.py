import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, sys
import mysql.connector
from threading import Thread

def run_sub_t1():
    os.system('py files\\subjects.py')
def run_sub():
    Thread(target=run_sub_t1).start()

def run_fac_t1():
    os.system('py files\\faculty.py')
def run_fac():
    Thread(target=run_fac_t1).start()

def run_tt_t1():
    try:
        os.system('py files\\select_dept_timetable.py')
    except Exception as e:
        pass

def run_tt():
    Thread(target=run_tt_t1).start()

def run_ab_t1():
    os.system('py files\\select_dept_batch.py')

def run_ab():
    Thread(target=run_ab_t1).start()

def run_time_t1():
    os.system('py files\\add_timing.py')

def run_time():
    Thread(target=run_time_t1).start()

try:
    root = Tk()

    root.title('Admin')
    root.geometry('900x500')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='binl\\bit.png')
    Label(root,image=img,bg='white').place(x=50,y=120)

    frame = Frame(root,width=350,height=480,bg="white")
    frame.place(x=480,y=70)

    heading = Label(frame,text='Admin Login', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=75,y=5)


    Button(frame,width=39,pady=7,text = 'Subjects',bg='#57a1f8',fg='white',border=0,command=run_sub).place(x=30,y=80)
    Button(frame,width=39,pady=7,text = 'Faculty',bg='#57a1f8',fg='white',border=0,command=run_fac).place(x=30,y=140)
    Button(frame,width=39,pady=7,text = 'Add Timings',bg='#57a1f8',fg='white',border=0,command=run_time).place(x=30,y=200)
    Button(frame,width=39,pady=7,text = 'Add Batch',bg='#57a1f8',fg='white',border=0,command=run_ab).place(x=30,y=260)
    Button(frame,width=39,pady=7,text = 'Set Timetable',bg='#57a1f8',fg='white',border=0,command=run_tt).place(x=30,y=320)
    Label(root,text='Created By : Divyanshu Jain',bg="#fff").place(x=710,y=470)
    root.mainloop()


except Exception as e:
    pass
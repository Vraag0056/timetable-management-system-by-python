import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import xlsxwriter
import xlrd
from collections import Counter
from tkinter.messagebox import askyesno

def ms_excel():
    old_path = "binl\\timetable.xlsx"
    old_workbook = xlrd.open_workbook(old_path)
    old_worksheet = old_workbook.sheet_by_index(0)


    all_row = []
    for row in range(old_worksheet.nrows):
        curr_row = []
        for col in range(old_worksheet.ncols):
            curr_row.append(old_worksheet.cell_value(row, col))
        all_row.append(curr_row)


    new_path = "timetable_excel\\timetable_cs.xlsx"
    workbook = xlsxwriter.Workbook(new_path)
    new_workseet = workbook.add_worksheet()

    bold_format = workbook.add_format({'bold': True})
    bold_format.set_align('top')
    bold_format.set_text_wrap()

    cell_format = workbook.add_format({'bold': True})
    cell_format.set_text_wrap()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')

    for row in range(len(all_row)):
        for col in range(len(all_row[0])):
            new_workseet.write(row, col, all_row[row][col], cell_format)

    index = 0
    m = 3
    l = 9
    for ln in range(0, 5):
        index = 0
        for row_index in range(m, l):
            new_workseet.write('B' + str(row_index), combo[ln][index].get(), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    index = 0
    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('C' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('D' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('F' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('G' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('I' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('J' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('K' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    m = 3
    l = 9
    for ln in range(0, 5):
        for row_index in range(m, l):
            new_workseet.write('L' + str(row_index), button[index].cget('text'), cell_format)
            index = index + 1
        m = m + 6
        l = l + 6

    new_workseet.set_column("A:L", 25)

    workbook.close()
    messagebox.showinfo("Sucess", "Excel file suceesfully created")


conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')
stu = conn.cursor()
s = f"SELECT subject_code from subjects"
stu.execute(s)
stu = list(stu)
fac = conn.cursor()
s = f"SELECT faculty_initials from faculty"
fac.execute(s)
fac = list(fac)

stu.insert(0,"Select Option")


init1_fac_mon=[]
init1_fac_tue=[]
init1_fac_wed=[]
init1_fac_thu=[]
init1_fac_fri=[]

init2_fac_mon=[]
init2_fac_tue=[]
init2_fac_wed=[]
init2_fac_thu=[]
init2_fac_fri=[]

init3_fac_mon=[]
init3_fac_tue=[]
init3_fac_wed=[]
init3_fac_thu=[]
init3_fac_fri=[]

init4_fac_mon=[]
init4_fac_tue=[]
init4_fac_wed=[]
init4_fac_thu=[]
init4_fac_fri=[]


init5_fac_mon=[]
init5_fac_tue=[]
init5_fac_wed=[]
init5_fac_thu=[]
init5_fac_fri=[]

init6_fac_mon=[]
init6_fac_tue=[]
init6_fac_wed=[]
init6_fac_thu=[]
init6_fac_fri=[]

init7_fac_mon=[]
init7_fac_tue=[]
init7_fac_wed=[]
init7_fac_thu=[]
init7_fac_fri=[]

init8_fac_mon=[]
init8_fac_tue=[]
init8_fac_wed=[]
init8_fac_thu=[]
init8_fac_fri=[]

init1_room_mon=[]
init1_room_tue=[]
init1_room_wed=[]
init1_room_thu=[]
init1_room_fri=[]

init2_room_mon=[]
init2_room_tue=[]
init2_room_wed=[]
init2_room_thu=[]
init2_room_fri=[]

init3_room_mon=[]
init3_room_tue=[]
init3_room_wed=[]
init3_room_thu=[]
init3_room_fri=[]

init4_room_mon=[]
init4_room_tue=[]
init4_room_wed=[]
init4_room_thu=[]
init4_room_fri=[]

init5_room_mon=[]
init5_room_tue=[]
init5_room_wed=[]
init5_room_thu=[]
init5_room_fri=[]

init6_room_mon=[]
init6_room_tue=[]
init6_room_wed=[]
init6_room_thu=[]
init6_room_fri=[]

init7_room_mon=[]
init7_room_tue=[]
init7_room_wed=[]
init7_room_thu=[]
init7_room_fri=[]

init8_room_mon=[]
init8_room_tue=[]
init8_room_wed=[]
init8_room_thu=[]
init8_room_fri=[]


def update_init_no():
    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=0 and btn_no<=5")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_mon.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=6 and btn_no<=11")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_tue.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=12 and btn_no<=17")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_wed.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=18 and btn_no<=23")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_thu.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=24 and btn_no<=29")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_fri.append(sch_f1[i][0])




    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=30 and btn_no<=35")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_mon.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=36 and btn_no<=41")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_tue.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=42 and btn_no<=47")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_wed.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=48 and btn_no<=53")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_thu.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=54 and btn_no<=59")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_fri.append(sch_f1[i][0])




    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=60 and btn_no<=65")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_mon.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=66 and btn_no<=71")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_tue.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=72 and btn_no<=77")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_wed.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=78 and btn_no<=83")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_thu.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=84 and btn_no<=89")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_fri.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=90 and btn_no<=95")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_mon.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=96 and btn_no<=101")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_tue.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=102 and btn_no<=107")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_wed.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=108 and btn_no<=113")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_thu.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=114 and btn_no<=119")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_fri.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=120 and btn_no<=125")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_mon.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=126 and btn_no<=131")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_tue.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=132 and btn_no<=137")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_wed.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=138 and btn_no<=143")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_thu.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=144 and btn_no<=149")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=150 and btn_no<=155")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=156 and btn_no<=161")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=162 and btn_no<=167")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=168 and btn_no<=173")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=174 and btn_no<=179")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=180 and btn_no<=185")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=186 and btn_no<=191")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=192 and btn_no<=197")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=198 and btn_no<=203")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=204 and btn_no<=209")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=210 and btn_no<=215")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=216 and btn_no<=221")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=222 and btn_no<=227")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=228 and btn_no<=233")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule where btn_no>=234 and btn_no<=239")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_fri.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=0 and btn_no<=5")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=6 and btn_no<=11")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=12 and btn_no<=17")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=18 and btn_no<=23")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=24 and btn_no<=29")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=30 and btn_no<=35")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=36 and btn_no<=41")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=42 and btn_no<=47")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=48 and btn_no<=53")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=54 and btn_no<=59")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=60 and btn_no<=65")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=66 and btn_no<=71")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=72 and btn_no<=77")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=78 and btn_no<=83")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=84 and btn_no<=89")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=90 and btn_no<=95")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=96 and btn_no<=101")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=102 and btn_no<=107")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=108 and btn_no<=113")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=114 and btn_no<=119")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=120 and btn_no<=125")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=125 and btn_no<=131")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=132 and btn_no<=137")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=138 and btn_no<=143")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=144 and btn_no<=149")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=150 and btn_no<=155")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=156 and btn_no<=161")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=162 and btn_no<=167")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=168 and btn_no<=173")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=174 and btn_no<=179")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=180 and btn_no<=185")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=186 and btn_no<=191")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=192 and btn_no<=197")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=198 and btn_no<=203")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=204 and btn_no<=209")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=210 and btn_no<=215")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=216 and btn_no<=221")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=222 and btn_no<=227")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=228 and btn_no<=233")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule where btn_no>=234 and btn_no<=239")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_fri.append(sch_f1[i][0])
    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=0 and btn_no<=5")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_mon.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=6 and btn_no<=11")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_tue.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=12 and btn_no<=17")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_wed.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=18 and btn_no<=23")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_thu.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=24 and btn_no<=29")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_fac_fri.append(sch_f1[i][0])




    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=30 and btn_no<=35")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_mon.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=36 and btn_no<=41")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_tue.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=42 and btn_no<=47")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_wed.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=48 and btn_no<=53")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_thu.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=54 and btn_no<=59")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_fac_fri.append(sch_f1[i][0])




    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=60 and btn_no<=65")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_mon.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=66 and btn_no<=71")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_tue.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=72 and btn_no<=77")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_wed.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=78 and btn_no<=83")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_thu.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=84 and btn_no<=89")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_fac_fri.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=90 and btn_no<=95")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_mon.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=96 and btn_no<=101")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_tue.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=102 and btn_no<=107")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_wed.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=108 and btn_no<=113")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_thu.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=114 and btn_no<=119")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_fac_fri.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=120 and btn_no<=125")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_mon.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=126 and btn_no<=131")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_tue.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=132 and btn_no<=137")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_wed.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=138 and btn_no<=143")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_thu.append(sch_f1[i][0])


    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=144 and btn_no<=149")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_fac_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=150 and btn_no<=155")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=156 and btn_no<=161")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=162 and btn_no<=167")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=168 and btn_no<=173")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=174 and btn_no<=179")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_fac_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=180 and btn_no<=185")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=186 and btn_no<=191")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=192 and btn_no<=197")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=198 and btn_no<=203")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=204 and btn_no<=209")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_fac_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=210 and btn_no<=215")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=216 and btn_no<=221")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=222 and btn_no<=227")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=228 and btn_no<=233")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT faculty FROM schedule_m where btn_no>=234 and btn_no<=239")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_fac_fri.append(sch_f1[i][0])



    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=0 and btn_no<=5")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=6 and btn_no<=11")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=12 and btn_no<=17")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=18 and btn_no<=23")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=24 and btn_no<=29")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init1_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=30 and btn_no<=35")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=36 and btn_no<=41")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=42 and btn_no<=47")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=48 and btn_no<=53")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=54 and btn_no<=59")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init2_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=60 and btn_no<=65")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=66 and btn_no<=71")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=72 and btn_no<=77")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=78 and btn_no<=83")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=84 and btn_no<=89")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init3_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=90 and btn_no<=95")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=96 and btn_no<=101")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=102 and btn_no<=107")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=108 and btn_no<=113")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=114 and btn_no<=119")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init4_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=120 and btn_no<=125")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=125 and btn_no<=131")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=132 and btn_no<=137")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=138 and btn_no<=143")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=144 and btn_no<=149")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init5_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=150 and btn_no<=155")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=156 and btn_no<=161")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=162 and btn_no<=167")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=168 and btn_no<=173")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=174 and btn_no<=179")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init6_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=180 and btn_no<=185")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=186 and btn_no<=191")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=192 and btn_no<=197")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=198 and btn_no<=203")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=204 and btn_no<=209")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init7_room_fri.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=210 and btn_no<=215")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_mon.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=216 and btn_no<=221")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_tue.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=222 and btn_no<=227")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_wed.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=228 and btn_no<=233")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_thu.append(sch_f1[i][0])

    sch_f1 = conn.cursor()
    sch_f1.execute("SELECT room FROM schedule_m where btn_no>=234 and btn_no<=239")
    sch_f1=list(sch_f1)
    for i in range(0,len(sch_f1)):
        if sch_f1[i][0] !='':
            init8_room_fri.append(sch_f1[i][0])






def update(var, j, x):
    root1 = Tk()
    root1.title('Set')
    root1.geometry('350x350')
    root1.configure(bg="#fff")
    root1.resizable(False, False)

    Label(root1, text="Day: " + days[j], fg='black', bg='white', borderwidth=3, width=25, relief="sunken",
          font=('Consolas', 18, 'bold')).place(x=5, y=10)
    Label(root1, text="Timing: " + time[x].get(), fg='black', bg='white', borderwidth=3, width=25, relief="sunken",
          font=('Consolas', 18, 'bold')).place(x=5, y=50)
    '''print('var: '+str(var))
    print('x: '+str(x))
    print('j: '+str(j))'''
    cur = conn.cursor()
    cur.execute(
        f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
    cur.execute("commit")
    com=''
    for key in range(0,6):
        if((var-key)%30==0 or (var-key)==0):
            com = combo[0][key].get()
            Label(root1, text="Course: "+combo[0][key].get(), fg='black', bg='white', borderwidth=3, width=25, relief="sunken",
                  font=('Consolas', 18, 'bold')).place(x=5, y=90)

    for key in range(0,6):
        if((var-key-6)%30==0 or (var-key-6)==0):
            com = combo[1][key].get()
            Label(root1, text="Course: "+combo[1][key].get(), fg='black', bg='white', borderwidth=3, width=25, relief="sunken",
                  font=('Consolas', 18, 'bold')).place(x=5, y=90)

    for key in range(0,6):
        if((var-key-12)%30==0 or (var-key-12)==0):
            com = combo[2][key].get()
            Label(root1, text="Course: "+combo[2][key].get(), fg='black', bg='white', borderwidth=3, width=25, relief="sunken",
                  font=('Consolas', 18, 'bold')).place(x=5, y=90)

    for key in range(0,6):
        if((var-key-18)%30==0 or (var-key-18)==0):
            com = combo[3][key].get()
            Label(root1, text="Course: "+combo[3][key].get(), fg='black', bg='white', borderwidth=3, width=25, relief="sunken",
                  font=('Consolas', 18, 'bold')).place(x=5, y=90)

    for key in range(0,6):
        if((var-key-24)%30==0 or (var-key-24)==0):
            com = combo[4][key].get()
            Label(root1, text="Course: "+combo[4][key].get(), fg='black', bg='white', borderwidth=3, width=25, relief="sunken",
                  font=('Consolas', 18, 'bold')).place(x=5, y=90)



    Label(root1, text="Subject:", fg='black', bg='white', borderwidth=3,
          font=('Consolas', 13, 'bold')).place(x=5, y=150)
    combo1 = ttk.Combobox(root1, width=24, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=stu
                          )
    combo1.current(0)
    combo1.place(x=130, y=150)


    Label(root1, text="Faculty:", fg='black', bg='white', borderwidth=3,
          font=('Consolas', 13, 'bold')).place(x=5, y=190)

    t = ''
    q = ''
    for i in range(len(button)):
        if i == var:
            if button[i].cget('text') == "free":
                t = 'free'
            else:
                t = button[i].cget('text')
                q = t[11:len(t)]
                t = t[6:9]


    '''print(t)
    print(q)'''

    if (x == 0 and j == 0 ):
        out = [item for t in fac for item in t]
        if t != 'free':
            if t in init1_fac_mon:
                init1_fac_mon.remove(t)
        if t != 'free':
            if q in init1_room_mon:
                init1_room_mon.remove(q)

        for kl in out[:]:
            if kl in init1_fac_mon:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)


    if (x == 0 and j == 1):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init1_room_tue:
                init1_room_tue.remove(q)
        if t != 'free':
            if t in init1_fac_tue:
                init1_fac_tue.remove(t)
        for kl in out[:]:
            if kl in init1_fac_tue:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 0 and j == 2):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init1_room_wed:
                init1_room_wed.remove(q)
        if t != 'free':
            if t in init1_fac_wed:
                init1_fac_wed.remove(t)
        for kl in out[:]:
            if kl in init1_fac_wed:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 0 and j == 3):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init1_room_thu:
                init1_room_thu.remove(q)
        if t != 'free':
            if t in init1_fac_thu:
                init1_fac_thu.remove(t)
        for kl in out[:]:
            if kl in init1_fac_thu:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 0 and j == 4):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init1_room_fri:
                init1_room_fri.remove(q)
        if t != 'free':
            if t in init1_fac_fri:
                init1_fac_fri.remove(t)
        for kl in out[:]:
            if kl in init1_fac_fri:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 1 and j == 0):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init2_room_mon:
                init2_room_mon.remove(q)
        if t != 'free':
            if t in init2_fac_mon:
                init2_fac_mon.remove(t)
        for kl in out[:]:
            if kl in init2_fac_mon:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 1 and j == 1):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init2_room_tue:
                init2_room_tue.remove(q)
        if t != 'free':
            if t in init2_fac_tue:
                init2_fac_tue.remove(t)
        for kl in out[:]:
            if kl in init2_fac_tue:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 1 and j == 2):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init2_room_wed:
                init2_room_wed.remove(q)
        if t != 'free':
            if t in init2_fac_wed:
                init2_fac_wed.remove(t)
        for kl in out[:]:
            if kl in init2_fac_wed:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 1 and j == 3):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init2_room_thu:
                init2_room_thu.remove(q)
        if t != 'free':
            if t in init2_fac_thu:
                init2_fac_thu.remove(t)
        for kl in out[:]:
            if kl in init2_fac_thu:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 1 and j == 4):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init2_room_fri:
                init2_room_fri.remove(q)
        if t != 'free':
            if t in init2_fac_fri:
                init2_fac_fri.remove(t)
        for kl in out[:]:
            if kl in init2_fac_fri:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 2 and j == 0):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init3_room_mon:
                init3_room_mon.remove(q)
        if t != 'free':
            if t in init3_fac_mon:
                init3_fac_mon.remove(t)
        for kl in out[:]:
            if kl in init3_fac_mon:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                          values=out
                          )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 2 and j == 1):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init3_room_tue:
                init3_room_tue.remove(q)
        if t != 'free':
            if t in init3_fac_tue:
                init3_fac_tue.remove(t)
        for kl in out[:]:
            if kl in init3_fac_tue:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=fac
                                  )
        combo2.current(0)

        combo2.place(x=130, y=190)

    if (x == 2 and j == 2):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init3_room_wed:
                init3_room_wed.remove(q)
        if t != 'free':
            if t in init3_fac_wed:
                init3_fac_wed.remove(t)
        for kl in out[:]:
            if kl in init3_fac_wed:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 2 and j == 3):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init3_room_thu:
                init3_room_thu.remove(q)
        if t != 'free':
            if t in init3_fac_thu:
                init3_fac_thu.remove(t)
        for kl in out[:]:
            if kl in init3_fac_thu:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 2 and j == 4):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init3_room_fri:
                init3_room_fri.remove(q)
        if t != 'free':
            if t in init3_fac_fri:
                init3_fac_fri.remove(t)
        for kl in out[:]:
            if kl in init3_fac_fri:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 3 and j == 0):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init4_room_mon:
                init4_room_mon.remove(q)
        if t != 'free':
            if t in init4_fac_mon:
                init4_fac_mon.remove(t)
        for kl in out[:]:

            if kl in init4_fac_mon:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 3 and j == 1):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init4_room_tue:
                init4_room_tue.remove(q)
        if t != 'free':
            if t in init4_fac_tue:
                init4_fac_tue.remove(t)
        for kl in out[:]:
            if kl in init4_fac_tue:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 3 and j == 2):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init4_room_wed:
                init4_room_wed.remove(q)
        if t != 'free':
            if t in init4_fac_wed:
                init4_fac_wed.remove(t)
        for kl in out[:]:
            if kl in init4_fac_wed:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 3 and j == 3):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init4_room_thu:
                init4_room_thu.remove(q)
        if t != 'free':
            if t in init4_fac_thu:
                init4_fac_thu.remove(t)
        for kl in out[:]:
            if kl in init4_fac_thu:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 3 and j == 4):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init4_room_fri:
                init4_room_fri.remove(q)
        if t != 'free':
            if t in init4_fac_fri:
                init4_fac_fri.remove(t)
        for kl in out[:]:
            if kl in init4_fac_fri:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 4 and j == 0):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init5_room_mon:
                init5_room_mon.remove(q)
        if t != 'free':
            if t in init5_fac_mon:
                init5_fac_mon.remove(t)
        for kl in out[:]:
            if kl in init5_fac_mon:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 4 and j == 1):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init5_room_tue:
                init5_room_tue.remove(q)
        if t != 'free':
            if t in init5_fac_tue:
                init5_fac_tue.remove(t)
        for kl in out[:]:
            if kl in init5_fac_tue:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 4 and j == 2):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init5_room_wed:
                init5_room_wed.remove(q)
        if t != 'free':
            if t in init5_fac_wed:
                init5_fac_wed.remove(t)
        for kl in out[:]:
            if kl in init5_fac_wed:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 4 and j == 3):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init5_room_thu:
                init5_room_thu.remove(q)
        if t != 'free':
            if t in init5_fac_thu:
                init5_fac_thu.remove(t)
        for kl in out[:]:
            if kl in init5_fac_thu:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 4 and j == 4):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init5_room_fri:
                init5_room_fri.remove(q)
        if t != 'free':
            if t in init5_fac_fri:
                init5_fac_fri.remove(t)
        for kl in out[:]:
            if kl in init5_fac_fri:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )

        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 5 and j == 0):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init6_room_mon:
                init6_room_mon.remove(q)
        if t != 'free':
            if t in init6_fac_mon:
                init6_fac_mon.remove(t)
        for kl in out[:]:
            if kl in init6_fac_mon:
                    out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                  values=out
                                  )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 5 and j == 1):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init6_room_tue:
                init6_room_tue.remove(q)
        if t != 'free':
            if t in init6_fac_tue:
                init6_fac_tue.remove(t)
        for kl in out[:]:
            if kl in init6_fac_tue:
                        out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 5 and j == 2):
        out = [item for t in fac for item in t]
        if t != 'free':
            if q in init6_room_wed:
                init6_room_wed.remove(q)
        if t != 'free':
            if t in init6_fac_wed:
                init6_fac_wed.remove(t)
        for kl in out[:]:
            if kl in init6_fac_wed:
                out.remove(kl)
        out.insert(0, "Select Option")
        combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
        combo2.current(0)
        combo2.place(x=130, y=190)

    if (x == 5 and j == 3):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init6_room_thu:
                    init6_room_thu.remove(q)
            if t != 'free':
                if t in init6_fac_thu:
                    init6_fac_thu.remove(t)
            for kl in out[:]:
                if kl in init6_fac_thu:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)

    if (x == 5 and j == 4):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init6_room_fri:
                    init6_room_fri.remove(q)
            if t != 'free':
                if t in init6_fac_fri:
                    init6_fac_fri.remove(t)
            for kl in out[:]:
                if kl in init6_fac_fri:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)


    if (x == 6 and j == 0):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init7_room_mon:
                    init7_room_mon.remove(q)
            if t != 'free':
                if t in init7_fac_mon:
                    init7_fac_mon.remove(t)
            for kl in out[:]:
                if kl in init7_fac_mon:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)

    if (x == 6 and j == 1):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init7_room_tue:
                    init7_room_tue.remove(q)
            if t != 'free':
                if t in init7_fac_tue:
                    init7_fac_tue.remove(t)
            for kl in out[:]:
                if kl in init7_fac_tue:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)

    if (x == 6 and j == 2):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init7_room_wed:
                    init7_room_wed.remove(q)
            if t != 'free':
                if t in init7_fac_wed:
                    init7_fac_wed.remove(t)
            for kl in out[:]:
                if kl in init7_fac_wed:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)

    if (x == 6 and j == 3):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init7_room_thu:
                    init7_room_thu.remove(q)
            if t != 'free':
                if t in init7_fac_thu:
                    init7_fac_thu.remove(t)
            for kl in out[:]:
                if kl in init7_fac_thu:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)

    if (x == 6 and j == 4):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init7_room_fri:
                    init7_room_fri.remove(q)
            if t != 'free':
                if t in init7_fac_fri:
                    init7_fac_fri.remove(t)
            for kl in out[:]:
                if kl in init7_fac_fri:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)

    if (x == 7 and j == 0):
            out = [item for t in fac for item in t]
            if t != 'free':
                if q in init8_room_mon:
                    init8_room_mon.remove(q)
            if t != 'free':
                if t in init8_fac_mon:
                    init8_fac_mon.remove(t)
            for kl in out[:]:
                if kl in init8_fac_mon:
                        out.remove(kl)
            out.insert(0, "Select Option")
            combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                      values=out
                                      )
            combo2.current(0)
            combo2.place(x=130, y=190)

    if (x == 7 and j == 1):
                out = [item for t in fac for item in t]
                if t != 'free':
                    if q in init8_room_tue:
                        init8_room_tue.remove(q)
                if t != 'free':
                    if t in init8_fac_tue:
                        init8_fac_tue.remove(t)
                for kl in out[:]:
                    if kl in init8_fac_tue:
                        out.remove(kl)
                out.insert(0, "Select Option")
                combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                          values=out
                                          )
                combo2.current(0)
                combo2.place(x=130, y=190)

    if (x == 7 and j == 2):
                out = [item for t in fac for item in t]
                if t != 'free':
                    if q in init8_room_wed:
                        init8_room_wed.remove(q)
                if t != 'free':
                    if t in init8_fac_wed:
                        init8_fac_wed.remove(t)
                for kl in out[:]:
                    if kl in init8_fac_wed:
                            out.remove(kl)
                out.insert(0, "Select Option")
                combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                          values=out
                                          )
                combo2.current(0)
                combo2.place(x=130, y=190)

    if (x == 7 and j == 3):
                out = [item for t in fac for item in t]
                if t != 'free':
                    if q in init8_room_thu:
                        init8_room_thu.remove(q)
                if t != 'free':
                    if t in init8_fac_thu:
                        init8_fac_thu.remove(t)
                for kl in out[:]:
                    if kl in init8_fac_thu:
                        out.remove(kl)
                out.insert(0, "Select Option")
                combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                          values=out
                                          )
                combo2.current(0)
                combo2.place(x=130, y=190)

    if (x == 7 and j == 4):
                out = [item for t in fac for item in t]
                if t != 'free':
                    if q in init8_room_fri:
                        init8_room_fri.remove(q)
                if t != 'free':
                    if t in init8_fac_fri:
                        init8_fac_fri.remove(t)
                for kl in out[:]:
                    if kl in init8_fac_fri:
                            out.remove(kl)
                out.insert(0, "Select Option")
                combo2 = ttk.Combobox(root1, width=25, font=('Microsoft YaHei UI Light', 9), state='readonly',
                                          values=out
                                          )
                combo2.current(0)
                combo2.place(x=130, y=190)

    Label(root1, text="Room:", fg='black', bg='white', borderwidth=3,
          font=('Consolas', 13, 'bold')).place(x=5, y=230)
    room = tk.Entry(
        root1,
        font=('Consolas', 15),
        width=17
    )
    room.place(x=130, y=230)



    button[var].config(text="free")
    Button(root1, width=39, pady=7, text='Set', bg='#57a1f8', fg='white', border=0,
           command=lambda var=var, stu_c=combo1,q=q,t=t, fac_ini=combo2, room=room, j=j, x=x, root1=root1: change(var, fac_ini,
                                                                                                          stu_c, room,
                                                                                                          j, x,q,t,com,
                                                                                                          root1)).place(
        x=35,
        y=280)

    root1.mainloop()

b=[]
def get_bat_com(i,j,k):

    b.clear()
    b.extend(batch)
    b.insert(0, "Select Option")

    for lq in range(i + k, j + k, 30):
        sch_f1 = conn.cursor()
        sch_f1.execute(f"SELECT course FROM schedule where btn_no={lq}")
        sch_f1 = list(sch_f1)
        if sch_f1[0][0] != '':
            b.pop(0)
            b.insert(0, sch_f1[0][0])
            break
    return b

def check_p(x,j,room,q,t):

    if (x == 0 and j == 0):
        if t != 'free':
            if q in init1_room_mon:
                init1_room_mon.remove(q)
        for i in init1_room_mon:
            if i == room:
                return False
        return True

    if (x == 0 and j == 1):
        if t != 'free':
           # print(q)
            if q in init1_room_tue:
                init1_room_tue.remove(q)
        for i in init1_room_tue:
            if i == room:
                return False
        return True

    if (x == 0 and j == 2):
        if t != 'free':
            if q in init1_room_wed:
                init1_room_wed.remove(q)
        for i in init1_room_wed:
            if i == room:
                return False
        return True

    if (x == 0 and j == 3):
        if t != 'free':
            if q in init1_room_thu:
                init1_room_thu.remove(q)
        for i in init1_room_thu:
            if i == room:
                return False
        return True

    if (x == 0 and j == 4):
        if t != 'free':
            if q in init1_room_fri:
                init1_room_fri.remove(q)
        for i in init1_room_fri:
            if i == room:
                return False
        return True

    if (x == 1 and j == 0):
        if t != 'free':
            if q in init2_room_mon:
                init2_room_mon.remove(q)
        for i in init2_room_mon:
            if i == room:
                return False
        return True

    if (x == 1 and j == 1):
        if t != 'free':
            if q in init2_room_tue:
                init2_room_tue.remove(q)
        for i in init2_room_tue:
            if i == room:
                return False
        return True

    if (x == 1 and j == 2):
        if t != 'free':
            if q in init2_room_wed:
                init2_room_wed.remove(q)
        for i in init2_room_wed:
            if i == room:
                return False
        return True

    if (x == 1 and j == 3):
        if t != 'free':
            if q in init2_room_thu:
                init2_room_thu.remove(q)
        for i in init2_room_thu:
            if i == room:
                return False
        return True



    if (x == 1 and j == 4):
        if t != 'free':
            if q in init2_room_fri:
                init2_room_fri.remove(q)
        for i in  init2_room_fri:
            if i == room:
                return False
        return True


    if (x == 2 and j == 0):
        if t != 'free':
            if q in init3_room_mon:
                init3_room_mon.remove(q)
        for i in init3_room_mon:
            if i == room:
                return False
        return True


    if (x == 2 and j == 1):
        if t != 'free':
            if q in init3_room_tue:
                init3_room_tue.remove(q)
        for i in init3_room_tue:
            if i == room:
                return False
        return True


    if (x == 2 and j == 2):
        if t != 'free':
            if q in init3_room_wed:
                init3_room_wed.remove(q)
        for i in init3_room_wed:
            if i == room:
                return False
        return True


    if (x == 2 and j == 3):
        if t != 'free':
            if q in init3_room_thu:
                init3_room_thu.remove(q)
        for i in init3_room_thu:
            if i == room:
                return False
        return True


    if (x == 2 and j == 4):
        if t != 'free':
            if q in init3_room_fri:
                init3_room_fri.remove(q)
        for i in init3_room_fri:
            if i == room:
                return False
        return True


    if (x == 3 and j == 0):
        if t != 'free':
            if q in init4_room_mon:
                init4_room_mon.remove(q)
        for i in init4_room_mon:
            if i == room:
                return False
        return True


    if (x == 3 and j == 1):
        if t != 'free':
            if q in init4_room_tue:
                init4_room_tue.remove(q)
        for i in init4_room_tue:
            if i == room:
                return False
        return True


    if (x == 3 and j == 2):
        if t != 'free':
            if q in init4_room_wed:
                init4_room_wed.remove(q)
        for i in init4_room_wed:
            if i == room:
                return False
        return True


    if (x == 3 and j == 3):
        if t != 'free':
            if q in init4_room_thu:
                init4_room_thu.remove(q)
        for i in init4_room_thu:
            if i == room:
                return False
        return True


    if (x == 3 and j == 4):
        if t != 'free':
            if q in init4_room_fri:
                init4_room_fri.remove(q)
        for i in init4_room_fri:
            if i == room:
                return False
        return True


    if (x == 4 and j == 0):
        if t != 'free':
            if q in init5_room_mon:
                init5_room_mon.remove(q)
        for i in init5_room_mon:
            if i == room:
                return False
        return True


    if (x == 4 and j == 1):
        if t != 'free':
            if q in init5_room_tue:
                init5_room_tue.remove(q)
        for i in init5_room_tue:
            if i == room:
                return False
        return True


    if (x == 4 and j == 2):
        if t != 'free':
            if q in init5_room_wed:
                init5_room_wed.remove(q)
        for i in init5_room_wed:
            if i == room:
                return False
        return True


    if (x == 4 and j == 3):
        if t != 'free':
            if q in init5_room_thu:
                init5_room_thu.remove(q)
        for i in init5_room_thu:
            if i == room:
                return False
        return True


    if (x == 4 and j == 4):
        if t != 'free':
            if q in init5_room_fri:
                init5_room_fri.remove(q)
        for i in init5_room_fri:
            if i == room:
                return False
        return True


    if (x == 5 and j == 0):
        if t != 'free':
            if q in init6_room_mon:
                init6_room_mon.remove(q)
        for i in init6_room_mon:
            if i == room:
                return False
        return True


    if (x == 5 and j == 1):
        if t != 'free':
            if q in init6_room_tue:
                init6_room_tue.remove(q)
        for i in init6_room_tue:
            if i == room:
                return False
        return True


    if (x == 5 and j == 2):
        if t != 'free':
            if q in init6_room_wed:
                init6_room_wed.remove(q)
        for i in init6_room_wed:
            if i == room:
                return False
        return True


    if (x == 5 and j == 3):
        if t != 'free':
            if q in init6_room_thu:
                init6_room_thu.remove(q)
        for i in init6_room_thu:
            if i == room:
                return False
        return True


    if (x == 5 and j == 4):
        if t != 'free':
            if q in init6_room_fri:
                init6_room_fri.remove(q)
        for i in init6_room_fri:
            if i == room:
                return False
        return True


    if (x == 6 and j == 0):
        if t != 'free':
            if q in init7_room_mon:
                init7_room_mon.remove(q)
        for i in init7_room_mon:
            if i == room:
                return False
        return True


    if (x == 6 and j == 1):
        if t != 'free':
            if q in init7_room_tue:
                init7_room_tue.remove(q)
        for i in init7_room_tue:
            if i == room:
                return False
        return True


    if (x == 6 and j == 2):
        if t != 'free':
            if q in init7_room_wed:
                init7_room_wed.remove(q)
        for i in init7_room_wed:
            if i == room:
                return False
        return True


    if (x == 6 and j == 3):
        if t != 'free':
            if q in init7_room_thu:
                init7_room_thu.remove(q)
        for i in init7_room_thu:
            if i == room:
                return False
        return True


    if (x == 6 and j == 4):
        if t != 'free':
            if q in init7_room_fri:
                init7_room_fri.remove(q)
        for i in init7_room_fri:
            if i == room:
                return False
        return True


    if (x == 7 and j == 0):
        if t != 'free':
            if q in init8_room_mon:
                init8_room_mon.remove(q)
        for i in init8_room_mon:
            if i == room:
                return False
        return True


    if (x == 7 and j == 1):
        if t != 'free':
            if q in init8_room_tue:
                init8_room_tue.remove(q)
        for i in init8_room_tue:
            if i == room:
                return False
        return True


    if (x == 7 and j == 2):
        if t != 'free':
            if q in init8_room_wed:
                init8_room_wed.remove(q)
        for i in init8_room_wed:
            if i == room:
                return False
        return True


    if (x == 7 and j == 3):
        if t != 'free':
            if q in init8_room_thu:
                init8_room_thu.remove(q)
        for i in init8_room_thu:
            if i == room:
                return False
        return True


    if (x == 7 and j == 4):
        if t != 'free':
            if q in init8_room_fri:
                init8_room_fri.remove(q)
        for i in init8_room_fri:
            if i == room:
                return False
        return True


def change(var, fac_ini, sub_c, room, j, x,q,t,com, root1):
    lmq=0
    answer = False
    d=Counter()

    if sub_c.get()=="Select Option" or fac_ini.get()=="Select Option" or room.get()=="":
        messagebox.showinfo("Failed", "Please fill all the options")
    else:
        alfa=check_p(x,j,room.get(),q,t)
        if alfa == True :
            for i in range(len(button)):
                if i == var:
                    button[i].config(text=sub_c.get() + '(' + fac_ini.get() + ')-' + room.get(), font=('Consolas', 10, 'bold'))
                    if(x==0 and j==0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()]>2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init1_room_mon.append(room.get())
                                init1_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init1_room_mon.append(room.get())
                            init1_fac_mon.append(fac_ini.get())


                    if (x == 0 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init1_room_tue.append(room.get())
                                init1_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:

                            init1_room_tue.append(room.get())
                            init1_fac_tue.append(fac_ini.get())

                    if (x == 0 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init1_room_wed.append(room.get())
                                init1_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init1_room_wed.append(room.get())
                            init1_fac_wed.append(fac_ini.get())

                    if (x == 0 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init1_room_thu.append(room.get())
                                init1_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init1_room_thu.append(room.get())
                            init1_fac_thu.append(fac_ini.get())

                    if (x == 0 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init1_room_fri.append(room.get())
                                init1_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init1_room_fri.append(room.get())
                            init1_fac_fri.append(fac_ini.get())

                    if (x == 1 and j == 0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                       # print(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init2_room_mon.append(room.get())
                                init2_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init2_room_mon.append(room.get())
                            init2_fac_mon.append(fac_ini.get())

                    if (x == 1 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init2_room_tue.append(room.get())
                                init2_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init2_room_tue.append(room.get())
                            init2_fac_tue.append(fac_ini.get())

                    if (x == 1 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init2_room_wed.append(room.get())
                                init2_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init2_room_wed.append(room.get())
                            init2_fac_wed.append(fac_ini.get())

                    if (x == 1 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init2_room_thu.append(room.get())
                                init2_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init2_room_thu.append(room.get())
                            init2_fac_thu.append(fac_ini.get())

                    if (x == 1 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init2_room_fri.append(room.get())
                                init2_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init2_room_fri.append(room.get())
                            init2_fac_fri.append(fac_ini.get())

                    if (x == 2 and j == 0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                       # print(d)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init3_room_mon.append(room.get())
                                init3_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init3_room_mon.append(room.get())
                            init3_fac_mon.append(fac_ini.get())

                    if (x == 2 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init3_room_tue.append(room.get())
                                init3_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:

                            init3_room_tue.append(room.get())
                            init3_fac_tue.append(fac_ini.get())

                    if (x == 2 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init3_room_wed.append(room.get())
                                init3_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init3_room_wed.append(room.get())
                            init3_fac_wed.append(fac_ini.get())

                    if (x == 2 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f1 for item in t]
                        sch_f2 = [i for i in sch_f1 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init3_room_thu.append(room.get())
                                init3_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init3_room_thu.append(room.get())
                            init3_fac_thu.append(fac_ini.get())

                    if (x == 2 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init3_room_fri.append(room.get())
                                init3_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init3_room_fri.append(room.get())
                            init3_fac_fri.append(fac_ini.get())

                    if (x == 3 and j == 0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        ''' print(d)
                        print(sch_f1)'''
                        if d[fac_ini.get()] >2:
                            lmq=2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init4_room_mon.append(room.get())
                                init4_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init4_room_mon.append(room.get())
                            init4_fac_mon.append(fac_ini.get())

                    if (x == 3 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init4_room_tue.append(room.get())
                                init4_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init4_room_tue.append(room.get())
                            init4_fac_tue.append(fac_ini.get())

                    if (x == 3 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init4_room_wed.append(room.get())
                                init4_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init4_room_wed.append(room.get())
                            init4_fac_wed.append(fac_ini.get())

                    if (x == 3 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init4_room_thu.append(room.get())
                                init4_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init4_room_thu.append(room.get())
                            init4_fac_thu.append(fac_ini.get())

                    if (x == 3 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init4_room_fri.append(room.get())
                                init4_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init4_room_fri.append(room.get())
                            init4_fac_fri.append(fac_ini.get())

                    if (x == 4 and j == 0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init5_room_mon.append(room.get())
                                init5_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init5_room_mon.append(room.get())
                            init5_fac_mon.append(fac_ini.get())

                    if (x == 4 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init5_room_tue.append(room.get())
                                init5_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init5_room_tue.append(room.get())
                            init5_fac_tue.append(fac_ini.get())

                    if (x == 4 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init5_room_wed.append(room.get())
                                init5_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init5_room_wed.append(room.get())
                            init5_fac_wed.append(fac_ini.get())

                    if (x == 4 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init5_room_thu.append(room.get())
                                init5_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init5_room_thu.append(room.get())
                            init5_fac_thu.append(fac_ini.get())

                    if (x == 4 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f1 for item in t]
                        sch_f2 = [i for i in sch_f1 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init5_room_fri.append(room.get())
                                init5_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init5_room_fri.append(room.get())
                            init5_fac_fri.append(fac_ini.get())

                    if (x == 5 and j == 0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init6_room_mon.append(room.get())
                                init6_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init6_room_mon.append(room.get())
                            init6_fac_mon.append(fac_ini.get())

                    if (x == 5 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init6_room_tue.append(room.get())
                                init6_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init6_room_tue.append(room.get())
                            init6_fac_tue.append(fac_ini.get())

                    if (x == 5 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init6_room_wed.append(room.get())
                                init6_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init6_room_wed.append(room.get())
                            init6_fac_wed.append(fac_ini.get())

                    if (x == 5 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init6_room_thu.append(room.get())
                                init6_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init6_room_thu.append(room.get())
                            init6_fac_thu.append(fac_ini.get())

                    if (x == 5 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init6_room_fri.append(room.get())
                                init6_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init6_room_fri.append(room.get())
                            init6_fac_fri.append(fac_ini.get())

                    if (x == 6 and j == 0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init7_room_mon.append(room.get())
                                init7_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init7_room_mon.append(room.get())
                            init7_fac_mon.append(fac_ini.get())

                    if (x == 6 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init7_room_tue.append(room.get())
                                init7_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init7_room_tue.append(room.get())
                            init7_fac_tue.append(fac_ini.get())

                    if (x == 6 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init7_room_wed.append(room.get())
                                init7_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init7_room_wed.append(room.get())
                            init7_fac_wed.append(fac_ini.get())

                    if (x == 6 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init7_room_thu.append(room.get())
                                init7_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init7_room_thu.append(room.get())
                            init7_fac_thu.append(fac_ini.get())

                    if (x == 6 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init7_room_fri.append(room.get())
                                init7_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init7_room_fri.append(room.get())
                            init7_fac_fri.append(fac_ini.get())

                    if (x == 7 and j == 0):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=0 and btn_no<=5) or (btn_no>=30 and btn_no<=35) or (btn_no>=60 and btn_no<=65) or (btn_no>=90 and btn_no<=95) or (btn_no>=120 and btn_no<=125) or (btn_no>=150 and btn_no<=155) or (btn_no>=180 and btn_no<=185) or (btn_no>=210 and btn_no<=215)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init8_room_mon.append(room.get())
                                init8_fac_mon.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init8_room_mon.append(room.get())
                            init8_fac_mon.append(fac_ini.get())

                    if (x == 7 and j == 1):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=6 and btn_no<=11) or (btn_no>=36 and btn_no<=41) or (btn_no>=66 and btn_no<=71) or (btn_no>=96 and btn_no<=101) or (btn_no>=126 and btn_no<=131) or (btn_no>=156 and btn_no<=161) or (btn_no>=186 and btn_no<=191) or (btn_no>=216 and btn_no<=221)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init8_room_tue.append(room.get())
                                init8_fac_tue.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init8_room_tue.append(room.get())
                            init8_fac_tue.append(fac_ini.get())

                    if (x == 7 and j == 2):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=12 and btn_no<=17) or (btn_no>=42 and btn_no<=47) or (btn_no>=72 and btn_no<=77) or (btn_no>=102 and btn_no<=107) or (btn_no>=132 and btn_no<=137) or (btn_no>=162 and btn_no<=167) or (btn_no>=192 and btn_no<=197) or (btn_no>=222 and btn_no<=227)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init8_room_wed.append(room.get())
                                init8_fac_wed.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init8_room_wed.append(room.get())
                            init8_fac_wed.append(fac_ini.get())

                    if (x == 7 and j == 3):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=18 and btn_no<=23) or (btn_no>=48 and btn_no<=53) or (btn_no>=78 and btn_no<=83) or (btn_no>=108 and btn_no<=113) or (btn_no>=138 and btn_no<=143) or (btn_no>=168 and btn_no<=173) or (btn_no>=198 and btn_no<=203) or (btn_no>=228 and btn_no<=233)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init8_room_thu.append(room.get())
                                init8_fac_thu.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:
                            init8_room_thu.append(room.get())
                            init8_fac_thu.append(fac_ini.get())

                    if (x == 7 and j == 4):
                        sch_f1 = conn.cursor()
                        sch_f1.execute(
                            f"SELECT faculty FROM schedule where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f1 = list(sch_f1)
                        sch_f1 = [item for t in sch_f1 for item in t]
                        sch_f1 = [i for i in sch_f1 if i != '']
                        sch_f2 = conn.cursor()
                        sch_f2.execute(
                            f"SELECT faculty FROM schedule_m where (btn_no>=24 and btn_no<=29) or (btn_no>=54 and btn_no<=59) or (btn_no>=84 and btn_no<=89) or (btn_no>=114 and btn_no<=119) or (btn_no>=144 and btn_no<=149) or (btn_no>=174 and btn_no<=179) or (btn_no>=204 and btn_no<=209) or (btn_no>=234 and btn_no<=239)")
                        sch_f2 = list(sch_f2)
                        sch_f2 = [item for t in sch_f2 for item in t]
                        sch_f2 = [i for i in sch_f2 if i != '']
                        sch_f1.extend(sch_f2)
                        d = Counter(sch_f1)
                        if d[fac_ini.get()] >2:
                            lmq = 2058
                            answer = askyesno(title='Confirm',
                                              message=f"'{fac_ini.get()}' have already 3 or more classes,do you want to add one more class?")
                            if answer:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                init8_room_fri.append(room.get())
                                init8_fac_fri.append(fac_ini.get())
                            else:
                                cur = conn.cursor()
                                cur.execute(
                                    f"UPDATE schedule SET day='',timing='',course='',subject='',faculty='',room='' WHERE  btn_no= '{var}'")
                                cur.execute("commit")
                                button[i].config(text="free",
                                                 font=('Consolas', 10, 'bold'))
                        else:

                            init8_room_fri.append(room.get())
                            init8_fac_fri.append(fac_ini.get())



                    if lmq!=2058:
                            cur = conn.cursor()
                            cur.execute(
                                f"UPDATE schedule SET day='{days[j]}',timing='{time[x].get()}',course='{com}',subject='{sub_c.get()}',faculty='{fac_ini.get()}',room='{room.get()}' WHERE  btn_no= '{var}'")
                            cur.execute("commit")

            root1.destroy()

        else:
            root1.destroy()
            messagebox.showerror("Message", "Room No. is already being occupied at this time")


root = Tk()
root.title('Set Timetable ---- CS Department')
root.geometry('1900x700')
root.configure(bg="#fff")
root.state("zoomed")
main_frame = Frame(root, width=500,
                   height=400)
main_frame.pack(fill=BOTH, expand=True)

my_canvas = Canvas(main_frame,
                   bg='#4A7A8C',
                   width=500,
                   height=400,
                   scrollregion=(0, 0, 700, 700))

scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
horizontal_scroll = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
horizontal_scroll.pack(side=BOTTOM, fill=X)
my_canvas.config(width=500, height=400)
my_canvas.config(yscrollcommand=scrollbar.set, xscrollcommand=horizontal_scroll.set)

my_canvas.pack(side=LEFT, fill=BOTH, expand=True)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

Label(second_frame, text='Day', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=0, padx=(0, 10))
Label(second_frame, text='Batch', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=1, padx=(0, 12))
Label(second_frame, text='Lecture 1', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=3, padx=(0, 12))
Label(second_frame, text='Lecture 2', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=4, padx=(0, 12))
Label(second_frame, text='break', fg='black', bg='white', borderwidth=3, width=5, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=5, padx=(0, 12))
Label(second_frame, text='Lecture 3', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=6, padx=(0, 12))
Label(second_frame, text='Lecture 4', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=7, padx=(0, 12))
Label(second_frame, text='break', fg='black', bg='white', borderwidth=3, width=5, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=8, padx=(0, 12))
Label(second_frame, text='Lecture 5', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=9, padx=(0, 12))
Label(second_frame, text='Lecture 6', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=10, padx=(0, 12))
Label(second_frame, text='Lecture 7', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=11, padx=(0, 12))
Label(second_frame, text='Lecture 8', fg='black', bg='white', borderwidth=3, width=10, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=0, column=12, padx=(0, 12))

x = (300, 450, 685, 835, 1070, 1220, 1370, 1520)
y = (100, 175, 250, 325, 400)
time = []
conn = mysql.connector.connect(host='localhost', user='root', password='root', database='timetable')
lec = conn.cursor()
s = f"SELECT time from timing"
lec.execute(s)
lec = list(lec)
time1 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time1.insert(0,lec[0][0])
time1.config(state= "disabled")
time1.place(x=300, y=50)
time.append(time1)
time2 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time.append(time2)
time2.insert(0,lec[1][0])
time2.config(state= "disabled")
time2.place(x=450, y=50)

break1_time = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=6, borderwidth=3,
)
break1_time.insert(0,lec[8][0])
break1_time.config(state= "disabled")
break1_time.place(x=600, y=50)
time3 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time3.insert(0,lec[2][0])
time3.config(state= "disabled")
time3.place(x=685, y=50)
time.append(time3)
time4 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time4.insert(0,lec[3][0])
time4.config(state= "disabled")
time4.place(x=835, y=50)
time.append(time4)
break2_time = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=6, borderwidth=3,
)
break2_time.insert(0,lec[9][0])
break2_time.config(state= "disabled")
break2_time.place(x=985, y=50)

time5 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time5.insert(0,lec[4][0])
time5.config(state= "disabled")
time5.place(x=1070, y=50)
time.append(time5)
time6 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time6.insert(0,lec[5][0])
time6.config(state= "disabled")
time6.place(x=1220, y=50)
time.append(time6)
time7 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time7.insert(0,lec[6][0])
time7.config(state= "disabled")
time7.place(x=1370, y=50)
time.append(time7)
time8 = tk.Entry(
    second_frame,
    font=('Consolas', 15),
    width=12, borderwidth=3
)
time8.insert(0,lec[7][0])
time8.config(state= "disabled")
time8.place(x=1520, y=50)
time.append(time8)

Label(second_frame, text='Monday', fg='black', bg='white', borderwidth=3, width=10, height=7, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=1, column=0, pady=(70, 5), padx=0)
Label(second_frame, text='Tuesday', fg='black', bg='white', borderwidth=3, width=10, height=7, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=2, column=0, pady=5)
Label(second_frame, text='Wednesday', fg='black', bg='white', borderwidth=3, width=10, height=7, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=3, column=0, pady=5)
Label(second_frame, text='Thursday', fg='black', bg='white', borderwidth=3, width=10, height=7, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=4, column=0, pady=5)
Label(second_frame, text='Friday', fg='black', bg='white', borderwidth=3, width=10, height=7, relief="sunken",
      font=('Consolas', 18, 'bold')).grid(row=5, column=0, pady=5)

Label(second_frame, text='', height=3).grid(row=6, column=0, pady=5)

var = 0
l = 0
m = 0
button = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
batch = conn.cursor()
s = f"SELECT batch_name from batch"
batch.execute(s)
batch = list(batch)

combo = []
combo1 = []
lm = 120
lq=0
b = []
for k in range(0, 6):
    b=get_bat_com(0,211,k)

    combo1.append(ttk.Combobox(second_frame, width=15, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                               values=b
                               ))
    combo1[k].current(0)
    combo1[k].place(x=150, y=lm)
    lm = lm + 30

lm = 335
combo2 = []
for k in range(0, 6):
    b = get_bat_com(6, 217, k)
    combo2.append((ttk.Combobox(second_frame, width=15, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                                values=b
                                )))
    combo2[k].current(0)
    combo2[k].place(x=150, y=lm)
    lm = lm + 30

lm = 550
combo3 = []
for k in range(0, 6):
    b = get_bat_com(12, 223, k)
    combo3.append((ttk.Combobox(second_frame, width=15, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                                values=b
                                )))
    combo3[k].current(0)
    combo3[k].place(x=150, y=lm)
    lm = lm + 30

lm = 765
combo4 = []
for k in range(0, 6):
    b = get_bat_com(18, 229, k)
    combo4.append((ttk.Combobox(second_frame, width=15, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                                values=b
                                )))
    combo4[k].current(0)
    combo4[k].place(x=150, y=lm)
    lm = lm + 30

lm = 980
combo5 = []
for k in range(0, 6):
    b = get_bat_com(24, 235, k)
    combo5.append((ttk.Combobox(second_frame, width=15, font=('Microsoft YaHei UI Light', 9),state= 'readonly',
                                values=b
                                )))
    combo5[k].current(0)
    combo5[k].place(x=150, y=lm)
    lm = lm + 30

combo.append(combo1)
combo.append(combo2)
combo.append(combo3)
combo.append(combo4)
combo.append(combo5)

lm = 120

sch = conn.cursor()
sch.execute("SELECT subject,faculty,room FROM schedule")
sch=list(sch)
op=0
update_init_no()
for k in range(0, 8):
    lm = 120
    km = x[k]
    for i in range(0, 5):
        for j in range(0, 6):
            if sch[op][2]=='':
                btn = Button(second_frame, width=19, pady=2, text='free', bg='#57a1f8', fg='white', height='0', border=0,
                             command=lambda var=var, k=k, i=i: update(var, i, k))
                var = var + 1
                btn.place(x=km, y=lm)
                button.append(btn)
                lm = lm + 30
                op=op+1
            else:
                btn = Button(second_frame, width=19, pady=2, text=sch[op][0] + '(' + sch[op][1] + ')-' + sch[op][2], bg='#57a1f8', fg='white', height='0',
                             border=0, font=('Consolas', 10, 'bold'),
                             command=lambda var=var, k=k, i=i: update(var, i, k))
                var = var + 1
                btn.place(x=km, y=lm)
                button.append(btn)
                lm = lm + 30
                op=op+1

        lm = lm + 35

Label(second_frame, text='S\nH\nO\nR\nT\n-\nB\nR\nE\nA\nK', fg='black', bg='white', borderwidth=3, width=5, height=37,
      relief="sunken", font=('Consolas', 18, 'bold')).place(x=600, y=120)
Label(second_frame, text='L\nU\nN\nC\nH\n-\nB\nR\nE\nA\nK', fg='black', bg='white', borderwidth=3, width=5, height=37,
      relief="sunken", font=('Consolas', 18, 'bold')).place(x=985, y=120)

Button(second_frame, width=20, pady=7, text='convert into Excel', bg='#57a1f8', fg='white', border=0,
       command=ms_excel).place(x=20, y=1180)
Label(second_frame,text='Created By : Divyanshu Jain').place(x=1150,y=1200)

root.mainloop()
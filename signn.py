#signn.py

import mysql.connector as mydb
con=mydb.connect(host="localhost",user="root",password="123456",database="sit")
mycursor=con.cursor()
from tkinter import *
sign_up=Tk()
sign_up.geometry("600x400")

name = Label(sign_up, text="Name").grid(row=0, column=1)
rno = Label(sign_up, text="RollNo").grid(row=1, column=1)
age = Label(sign_up, text="Age").grid(row=2, column=1)
gender = Label(sign_up, text="Gender").grid(row=3, column=1)
passw = Label(sign_up, text="Password").grid(row=4, column=1)


namevalue = StringVar()
rnovalue = IntVar()
agevalue = IntVar()
gendervalue = StringVar()
passvalue = StringVar()

nameentry = Entry(sign_up, textvariable=namevalue).grid(row=0, column=2)
rnoentry = Entry(sign_up, textvariable=rnovalue).grid(row=1, column=2)
ageentry = Entry(sign_up, textvariable=agevalue).grid(row=2, column=2)
genderentry = Entry(sign_up, textvariable=gendervalue).grid(row=3, column=2)
passentry = Entry(sign_up, textvariable=passvalue).grid(row=4, column=2)

def values():
    a = namevalue.get()
    b = rnovalue.get()
    c = agevalue.get()
    d = gendervalue.get()
    e = passvalue.get()
    try:
        mycursor.execute("insert into tkinter values('{}',{},{},'{}','{}')".format(a, b, c, d,e))
         # mycursor.execute(f"insert into tkinter values('{a}','{b}','{c}','{d}')")
        con.commit()
    except:
        mycursor.execute("create table tkinter(Name Varchar(20),Rollno Int Unique,Age Int,Gender Char(1))")
        mycursor.execute("insert into tkinter values('{}',{},{},'{}')".format(a, b, c, d))
        con.commit()
b12=Button(text="Submit",command=values).grid(row=4,column=1)
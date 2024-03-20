from tkinter import *
from tkinter import messagebox
root = Tk()

import sqlite3
connect = sqlite3.Connection("Bus_Booking_System.db")

count1 = 0
def add1():
    c = connect.cursor()
    c.execute("INSERT INTO OPERATOR(Operator_ID,Opt_Name, Address , Email_ID,Phone_no) Values (?,?,?,?,?)",(id_ent.get(),name_ent.get(),address_ent.get(),email_ent.get(),phone_ent.get()))
    connect.commit()
    count1= count1 +1
    if count1 > 1:
        lab1.destroy()
    lab1 = Label(root, text= id_ent.get()+" "+name_ent.get()+" "+address_ent.get()+" "+email_ent.get()+" "+phone_ent.get(), font = 'Arian 12')
    lab1.grid(row= 11, column =3, columnspan = 5)
    messagebox.showinfo("success","Record added successfully")

def pop():
    c = connect.cursor()
    c.execute("update OPERATOR set Operator_ID=?,Opt_Name=?, Address =?, Email_ID=?,Phone_no=? where Operator_ID= ? ",(id_ent.get(),name_ent.get(),address_ent.get(),email_ent.get(),phone_ent.get(),id_ent.get()))
    connect.commit()
    

    lab2 = Label(root, text= id_ent.get()+" "+name_ent.get()+" "+address_ent.get()+" "+email_ent.get()+" "+phone_ent.get(), font = 'Arian 12')
    lab2.grid(row= 11, column =3, columnspan = 5)
    messagebox.showinfo("operator entry update", "operator record updated succesully")

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
            
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 12, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 0)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 20 bold')
title.grid(row = 2, column = 0, columnspan = 12)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

add_text = Label(root, text = "Add Bus Operator Details",  fg = "green", font = 'Arian 20 bold')
add_text.grid(row = 6, column = 0, columnspan = 12)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)


id_text = Label(root, text = "Operator id")
id_text.grid(row = 10, column = 0)

id_ent = Entry(root, width= 10)
id_ent.grid(row = 10, column =1)


name_text = Label(root, text = "Name")
name_text.grid(row = 10, column = 2)

name_ent = Entry(root)
name_ent.grid(row = 10, column =3)


address_text = Label(root, text = "Address")
address_text.grid(row = 10, column = 4)

address_ent = Entry(root)
address_ent.grid(row = 10, column =5)


phone_text = Label(root, text = "Phone")
phone_text.grid(row = 10, column = 6)

phone_ent = Entry(root)
phone_ent.grid(row = 10, column =7)


email_text = Label(root, text = "Email")
email_text.grid(row = 10, column = 8)

email_ent = Entry(root)
email_ent.grid(row = 10, column =9)

add_but = Button(root, text = "Add",command= add1, bg= "lightgreen")
add_but.grid(row =10, column = 10)

edit_but = Button(root, text = "Edit", bg = "lightgreen", command = pop)
edit_but.grid(row =10, column = 11)


blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)


houses = PhotoImage(file = ".\\home.png")
Button(root, image = houses).grid(row = 13, column = 8)

root.mainloop()

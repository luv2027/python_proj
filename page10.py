from tkinter import *
from tkinter import messagebox
root = Tk()
import sqlite3

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def add1():
    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()
    c.execute("INSERT INTO  RUN(Bus_ID, Date, Seat_Availavle) values(?,?,?)", (id_ent.get(), date_ent.get(), seat_ent.get()))
    connect.commit()
    lab1 = Label(root, text= id_ent.get()+" "+date_ent.get()+" "+seat_ent.get(), font = 'Arian 12')
    lab1.grid(row=11, column=2, columnspan = 4)
    messagebox.showinfo("run entry", "run record added")

def delete1():
    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()
    c.execute("delete from  RUN where Bus_ID=?", (id_ent.get(),))
    connect.commit()
    lab1 = Label(root, text= id_ent.get()+" "+date_ent.get()+" "+seat_ent.get(), font = 'Arian 12')
    lab1.grid(row=11, column=2, columnspan = 4)
    messagebox.showinfo("run entry", "run record deleted")

              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 10, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

title = Label(root, text = "Add Bus Running Details" , fg = 'green' , font = 'Arian 14 bold')
title.grid(row = 6, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

id_text = Label(root, text = "Bus Id")
id_text.grid(row=10, column=0)

id_ent = Entry(root)
id_ent.grid(row=10, column=1)

date_text = Label(root, text = "Running Date")
date_text.grid(row=10, column=2)

date_ent = Entry(root)
date_ent.grid(row=10, column=3)

seat_text = Label(root, text = "Seat Available")
seat_text.grid(row=10, column=4)

seat_ent = Entry(root)
seat_ent.grid(row=10, column=5)

add_but = Button(root, text = "Add Run", bg ="lightgreen", command = add1)
add_but.grid(row = 10, column = 6)

edit_but = Button(root, text = "Delete Run", bg = "lightgreen", command= delete1)
edit_but.grid(row = 10, column = 7)

blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 13, column = 0)

def close(e=1):
    root.destroy()
    import page2

house = PhotoImage(file = ".\\home.png")
house_but = Button(root, image=house, command = close)
house_but.grid(row = 14, column = 6)

root.mainloop()

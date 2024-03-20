from tkinter import *
from tkinter import messagebox
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))


import sqlite3


def pop():
    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()
    c.execute("INSERT INTO BUS(Bus_ID, Type, Capacity , Fare , Operator_ID, Route_ID) Values (?,?,?,?,?,?)",(ent_bus.get(),clicked.get(),cap_ent.get(),fare_ent.get(),opt_ent.get(),route_ent.get()))
   

    connect.commit()
    
    lab1 = Label(root, text= ent_bus.get()+" "+clicked.get()+" "+cap_ent.get()+" "+fare_ent.get()+" "+opt_ent.get()+" "+route_ent.get(), font = 'Arian 12')
    lab1.grid(row=11, column=4, columnspan = 5)
    messagebox.showinfo("bus entry", "Bus record added")

def edit():
    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()
    c.execute("update BUS set Bus_ID=?, Type=?, Capacity=? , Fare=? , Operator_ID=?, Route_ID=? where Bus_ID= ?",(ent_bus.get(),clicked.get(),cap_ent.get(),fare_ent.get(),opt_ent.get(),route_ent.get(),ent_bus.get()))
    connect.commit()
    
    lab1 = Label(root, text= ent_bus.get()+" "+clicked.get()+" "+cap_ent.get()+" "+fare_ent.get()+" "+opt_ent.get()+" "+route_ent.get(), font = 'Arian 12')
    lab1.grid(row=11, column=4, columnspan = 5)
    messagebox.showinfo("bus entry", "Bus record edited")


clicked = StringVar()
clicked.set("AC 2X2")
              
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

title = Label(root, text = "Add Bus Details" , fg = 'green' , font = 'Arian 14 bold')
title.grid(row = 6, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

add_bus = Label(root, text = "Bus ID")
add_bus.grid(row=10, column=0)

ent_bus = Entry(root)
ent_bus.grid(row=10, column=1)

type_bus = Label(root, text = "Bus Type")
type_bus.grid(row=10, column=2)

drop_bus = OptionMenu(root, clicked ,"AC 2X2", "AC 3X2", "Non AC2X2", "Non AC 3X2", "AC-Sleeper 2X1", "Non-AC SLeeper 2X1" )
drop_bus.grid(row=10, column=3)

capacity_text = Label(root, text = "Capacity")
capacity_text.grid(row=10, column=4)

cap_ent = Entry(root)
cap_ent.grid(row=10, column=5)

fare_text = Label(root, text = "Fare Rs")
fare_text.grid(row=10, column=6)

fare_ent = Entry(root)
fare_ent.grid(row=10, column=7)

opt_text = Label(root, text = "Operator ID")
opt_text.grid(row=10, column=8)

opt_ent = Entry(root)
opt_ent.grid(row=10, column=9)

route_text = Label(root, text = "Route ID")
route_text.grid(row=10, column=10)

route_ent = Entry(root)
route_ent.grid(row=10, column=11)

blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 13, column = 0)

    

add_but = Button(root, text = "Add Bus", command=pop)
add_but.grid(row = 14, column = 6)

edit_but = Button(root, text = "Edit Bus", command =edit)
edit_but.grid(row = 14, column = 7)

def close(e=1):
    root.destroy()
    import page2

house = PhotoImage(file = ".\\home.png")
house_but = Button(root, image=house,command = close)
house_but.grid(row = 14, column = 8)

root.mainloop()

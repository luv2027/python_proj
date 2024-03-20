from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()

def add1():
    
    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()
    c.execute("INSERT INTO ROUTE(Route_ID, Station_id, Station_Name) VALUES(?,?,?)",(route_ent.get(),id_ent.get(),station_ent.get()))
    connect.commit()
    
    lab1 = Label(root, text= route_ent.get()+" "+id_ent.get()+" "+station_ent.get(), font = 'Arian 12')
    lab1.grid(row=11, column=2, columnspan = 4)
    messagebox.showinfo("station entry", "station record added")

def delete1():
    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()
    c.execute("delete from  ROUTE where Route_ID=?" ,(route_ent.get(),))
    connect.commit()
    
    lab1 = Label(root, text= route_ent.get()+" "+id_ent.get()+" "+station_ent.get(), font = 'Arian 12')
    lab1.grid(row=11, column=2, columnspan = 4)
    messagebox.showinfo("station entry", "station record deleted")
    
h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
              
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

title = Label(root, text = "Add Bus Route Details" , fg = 'green' , font = 'Arian 14 bold')
title.grid(row = 6, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

route_text = Label(root, text = "Route Id")
route_text.grid(row=10, column=0)

route_ent = Entry(root)
route_ent.grid(row=10, column=1)

station_text = Label(root, text = "Station Name1")
station_text.grid(row=10, column=2)

station_ent = Entry(root)
station_ent.grid(row=10, column=3)

id_text = Label(root, text = "Station_id")
id_text.grid(row=10, column=4)

id_ent = Entry(root)
id_ent.grid(row=10, column=5)

add_but = Button(root, text = "Add Route", bg ="lightgreen", command = add1)
add_but.grid(row = 10, column = 7)

edit_but = Button(root, text = "Delete Route", fg = "red", bg = "lightgreen", command = delete1)
edit_but.grid(row = 10, column = 8)

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

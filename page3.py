from tkinter import *
from tkinter import messagebox
root = Tk()
import sqlite3

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

clicked = StringVar()
clicked.set("Male")

def sure():
    ans = messagebox.askyesno("bus confirmation", "Are you sure you want to book the bus?")
    if ans == 1:
        def close(e=1):
            root.destroy()
            import page4
            
        root.after(1,close)

def book():
    blank = Label(root, text = "                            " )
    blank.grid(row = 11, column = 0)

    blank = Label(root, text = "                            " )
    blank.grid(row = 12, column = 0)

    blank = Label(root, text = "                            " )
    blank.grid(row = 13, column = 0)

    blank = Label(root, text = "                            " )
    blank.grid(row = 14, column = 0)
    
    fill_label = Label(root, text = "Fill Passenger Details to book the bus ticket" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
    fill_label.grid(row = 15, column = 0, columnspan = 8)

    blank = Label(root, text = "                            " )
    blank.grid(row = 16, column = 0)

    name_text = Label(root, text = "Name")
    name_text.grid(row = 17, column=0)

    name_ent = Entry(root)
    name_ent.grid(row =17, column=1)

    gender_text = Label(root, text = "Gender")
    gender_text.grid(row = 17, column=2)

    gender_drop = OptionMenu(root, clicked , "Male", "Female", "Third Gender")
    gender_drop.grid(row = 17, column = 3)

    seats_text = Label(root, text = "No of Seats")
    seats_text.grid(row = 17, column=4)

    seats_ent = Entry(root)
    seats_ent.grid(row =17, column=5)

    mobile_text = Label(root, text = "Mobile No")
    mobile_text.grid(row = 17, column=6)

    mobile_ent = Entry(root)
    mobile_ent.grid(row =17, column=7)

    age_text = Label(root, text = "Age")
    age_text.grid(row = 17, column=8)

    age_ent = Entry(root)
    age_ent.grid(row =17, column=9)

    book_button = Button(root, text = "Book Seat", bg ="lightgreen", command = sure)
    book_button.grid(row = 17, column=10)

    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()

    c.execute("INSERT INTO BOOKING_HISTORY(Passengers_Name , Gender , No_of_seats , Mobile_no) VALUES(?,?,?,?)", (name_ent.get(),clicked.get(),seats_ent.get(),mobile_ent.get()))
    connect.commit()
    


def show():
    select_text = Label(root, text = "Select Bus", fg = "green")
    select_text.grid(row = 8, column=0)

    opt_text = Label(root, text = "Operator", fg = "green")
    opt_text.grid(row = 8, column=1)

    type_text = Label(root, text = "Bus Type", fg = "green")
    type_text.grid(row = 8, column=2)

    available_text = Label(root, text = "Available/Capacity", fg = "green")
    available_text.grid(row = 8, column=3)

    fare_text = Label(root, text = "Fare", fg = "green")
    fare_text.grid(row = 8, column=4)

    
    connect = sqlite3.Connection("Bus_Booking_System.db")
    c = connect.cursor()
    

    c.execute("select o.opt_name, b.type, r.seat_availavle, b.fare from route as ro, bus as b, operator as o, run as r where ro.route_id = b.route_id and b.operator_Id = o.operator_id and b.bus_id = r.bus_id and ro.station_name =? ", (ent_To.get(),))

    records = c.fetchone()
    print(records)
    count =1
    for record in records:
        Label(root, text = str(record), fg = "blue").grid(row=9, column=count)
        count = count+1
    connect.commit()
    
    
    blank = Label(root, text = "                            " )
    blank.grid(row = 9, column = 0)

    book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command = book)
    book_button.grid(row =10 , column= 6, columnspan=2)

              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 8, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 8)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)

title1 =Label(root, text = "Enter Journey Details", bg="lightgreen", fg = "darkgreen", font = "Arian 14 bold" )
title1.grid(row=4, column = 0, columnspan =8 )


blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

To_text = Label(root, text = "To")
To_text.grid(row = 6, column =0)

ent_To = Entry(root, width=20)
ent_To.grid(row = 6, column =1)

From_text = Label(root, text = "From")
From_text.grid(row = 6, column =2)

ent_From = Entry(root, width=20)
ent_From.grid(row = 6, column =3)

date_text = Label(root, text = "Journey Date")
date_text.grid(row = 6, column =4)

ent_date = Entry(root, width=20)
ent_date.grid(row = 6, column =5)

show_button = Button(root, text = "Show Bus", fg = "blue", bg ="green", command = show)
show_button.grid(row = 6, column =6)

house = PhotoImage(file = ".\\home.png")

def close1(e=1):
            root.destroy()
            import page2

def ref():   
        root.after(1,close1)

home_button = Button(root, image = house, command = ref)
home_button.grid(row =6 , column= 7)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)

root.mainloop()






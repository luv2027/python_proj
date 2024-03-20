from tkinter import *
from tkinter import messagebox
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 1, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 1, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

ticket_text = Label(root, text ="Bus Ticket")
ticket_text.grid(row = 6, column=1, columnspan=3)

final = LabelFrame(root)
final.grid(row = 7, column =1, columnspan=3)

passenger_text = Label(final, text = "Passenger: ")
passenger_text.grid(row =8, column=0)

seats_text = Label(final, text = "No of seats: ")
seats_text.grid(row =10, column=0)

age_text = Label(final, text = "Age: ")
age_text.grid(row =12, column=0)

travel_text = Label(final, text = "Travel On: ")
travel_text.grid(row =14, column=0)

seats_text = Label(final, text = "No of Seats: ")
seats_text.grid(row =16, column=0)

g_text = Label(final, text = "Gender: ")
g_text.grid(row =8, column=1)

phone_text = Label(final, text = "Phone: ")
phone_text.grid(row =10, column=1)

flare_text = Label(final, text = "Flare Rs: ")
flare_text.grid(row =12, column=1)

detail_text = Label(final, text = "Bus Detail: ")
detail_text.grid(row =14, column=1)

booked_text = Label(final, text = "Booked On: ")
booked_text.grid(row =16, column=1)

point_text = Label(final, text = "Boarding Point: ")
point_text.grid(row =18, column=1)

last_text = Label(final, text = "Total amount Rs X to be paid at the time of boarding the bus")
last_text.grid(row =20, column=1)

messagebox.showinfo("Success", "Seat Booked....")

def confirm():
    ans = messagebox.askyesno("Closing", "For closing Click Yes \n Goto Main Page Click No")
    if ans :
        root.destroy()
    else:
        def close():
            root.destroy()
            import page2
        root.after(1, close)

root.protocol("WM_DELETE_WINDOW", confirm)
root.mainloop()

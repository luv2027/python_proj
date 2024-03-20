from tkinter import *
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

def close(e=1):
    root.destroy()
    import page3
    
def nslide():
    root.after(1,close)

seat_booking = Button(root, text ="Seat Booking " ,command = nslide, fg = 'blue', bg ='lightgreen')
seat_booking.grid(row = 6, column = 0)

def close1(e=1):
    root.destroy()
    import page5
    
def secslide():
    root.after(1,close1)

check_booked_seat = Button(root, text ="Check Booked Seat",command = secslide, fg = 'blue', bg ='green')
check_booked_seat.grid(row = 6, column = 1)

def close2(e=1):
    root.destroy()
    import page6

def tslide():
    root.after(1,close2)

add_bus = Button(root, text ="Add Bus Details" ,command = tslide, fg = 'blue', bg ='darkgreen')
add_bus.grid(row = 6, column = 2)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)

admin = Label(root, text = "For Admin Only", fg = 'red')
admin.grid(row = 9, column =2)

root.mainloop()

from tkinter import *
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def check():
    final = LabelFrame(root)
    final.grid(row = 8, column =0, columnspan=3)

    passenger_text = Label(final, text = "Passenger: ")
    passenger_text.grid(row =9, column=0)

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

    last_text = Label(final, text = "Total amount Rs X to br paid at the time of boarding the bus")
    last_text.grid(row =20, column=0)
              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)


title1 = Label(root, text = "Check Your Booking" , fg = 'darkgreen' , bg = 'lightgreen', font = 'Arian 14 bold')
title1.grid(row = 4, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 6, column = 0)

mobile_text = Label(root, text = "Enter Your Mobile No: ")
mobile_text.grid(row =7, column =0)

mobile_ent = Entry(root)
mobile_ent.grid(row =7, column=1)

check_but = Button(root, text = "Check Booking", command = check)
check_but.grid(row = 7, column=2)



root.mainloop()
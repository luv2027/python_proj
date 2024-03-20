from tkinter import *
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

              
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

detail = Label(root, text = "Add New Details to Database", fg ="green", font = 'Arian 14 bold')
detail.grid(row = 6, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)

def close(e=1):
    root.destroy()
    import page7

def slide():
    root.after(1,close)

operator_but= Button(root, text ="New Operator",command= slide,  bg = "lightgreen")
operator_but.grid(row= 9, column=0)

def close1(e=1):
    root.destroy()
    import page8

def secslide():
    root.after(1,close1)

bus_but= Button(root, text ="New Bus",command= secslide, bg = "orange")
bus_but.grid(row= 9, column=1)

def close2(e=1):
    root.destroy()
    import page9

def tslide():
    root.after(1, close2)

route_but= Button(root, text ="New Route",command= tslide, bg = "lightblue")
route_but.grid(row= 9, column=2)

def close3(e=1):
    root.destroy()
    import page10

def fslide():
    root.after(1, close3)
    
run_but= Button(root, text ="New Run",command = fslide,  bg = "lightpink")
run_but.grid(row= 9, column=3)

root.mainloop()

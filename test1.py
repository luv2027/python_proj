from tkinter import *
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
          
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 0)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 20 bold')
title.grid(row = 2, column = 0, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

name = Label(root, text = "Name : Luv Patel ", fg = "blue")
name.grid(row = 6, column = 0, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)

er = Label(root, text =" Er: 211B429", fg = "blue")
er.grid(row =8, column =0, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

mobile = Label(root, text = "Mobile: 9834597833", fg = "blue")
mobile.grid(row = 10, column =0 , padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 13, column = 0)


submitted_to  = Label(root, text = "Submitted to: Dr. Mahesh Kumar", fg = "red", bg = "lightblue", font= 'Arian 14 bold')
submitted_to.grid(row = 14, column =0, padx = w//3)

project_learning = Label(root, text = "Project Based Learning" , fg ='red')
project_learning.grid(row = 15, column = 0, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 16, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 17, column = 0)

def close(e=1):
    root.destroy()
    import page2

root.bind('<KeyPress>', close)

root.mainloop()

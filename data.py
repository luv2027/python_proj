from tkinter import*
import sqlite3
from tkinter.messagebox import *
from datetime import date
con=sqlite3.connect('project_db')
cur=con.cursor()
cur.execute('select * from run')
res=cur.fetchall()
print(res)

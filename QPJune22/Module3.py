#Qn15a) How to draw a star shape in python turtle.
"""
import turtle

tk=turtle.Turtle()
for i in range(0,6):
    tk.forward(100)
    tk.right(144)
"""
#Qn16a) Write a Python GUI program to take birth date and output the age when a button is pressed.
"""
from tkinter import *
from datetime import datetime

win=Tk()

def calc():
    try:
        birth_date = t1.get()
        today=datetime.today()
        birth= datetime.strptime(birth_date,"%Y-%m-%d")
        age=today.year-birth.year - ((today.month-today.day)<(birth.month-birth.day))
        ans.config(text=f"Your age is: {age}")
    except ValueError:
        ans.config(text="Invalid date format! Use YYYY-MM-DD")

l1=Label(win,text="Enter the age:")
l1.place(x=30,y=50)
t1=Entry(win)
t1.place(x=30,y=80)
s1=Button(win,text="Submit",command=calc)
s1.place(x=30,y=120)
ans=Label(win,text="")
ans.place(x=30,y=150)

win.mainloop()
"""


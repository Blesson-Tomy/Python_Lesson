import tkinter
from tkinter.constants import *
from tkinter import *
from tkinter import messagebox
"""
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, Aromal! Happy Valentines Day")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()


parent = tkinter.Tk()
rb=Button(parent,text="Red", fg="red")
rb.pack(side=LEFT)
bb=Button(parent,text="blue", fg="blue")
bb.pack(side=TOP)
rb=Button(parent,text="GREEN", fg="green")
rb.pack(side=RIGHT)
rb=Button(parent,text="yellow", fg="yellow")
rb.pack(side=BOTTOM)
parent.mainloop()



parent =tkinter.Tk()
name=Label(parent,text="Name of Student: ").grid(row=0,column=0)
e1=Entry(parent).grid(row=0,column=1)
idnu=Label(parent,text="Student ID: ").grid(row=1,column=0)
e2=Entry(parent).grid(row=1,column=1)
password=Label(parent,text="Password: ").grid(row=2,column=0)
e3=Entry(parent).grid(row=2,column=1)

def onClick():
    messagebox.askyesno(parent,"Testing")
    Stringg=Entry.get(self="")
    print(Stringg)


submit=Button(parent,text="Submit",command=onClick).grid(row=4,column=0)





parent.mainloop()


"""
import turtle

t=turtle.Turtle()
t.screen.bgcolor("orange")
x=t.screen.window_height()
t.hideturtle()
print(x)
t.color("blue")
t.fillcolor("blue")
t.begin_fill()
for i in range(0,6):
    
    
    t.forward(100)
    t.right(60)

t.end_fill()






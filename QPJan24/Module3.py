#Qn5) Write a Python program to draw a hexagon using turtle graphics.

"""
import turtle

t=turtle.Turtle()
for i in range(0,6):
    t.forward(100)
    t.right(60)

"""

#Qn15a) write a python program to convert a color image to a grayscale image.

"""
from PIL import Image

im=Image.open("Hello.gif")
im=im.convert("RGB")


wid,hi=im.size

gr=Image.new("L",im.size)

for h in range(0,hi):
    for w in range(0,wid):
        r,g,b = im.getpixel((w,h))
        gray= int(0.2989*r + 0.5870*g + 0.1140*b)
        gr.putpixel((w,h),gray)

gr.save("NEW1.jpg")
gr.show()
"""

#Qn16a) Write Python GUI program to input two strings and output a concatenated string when a button is pressed
"""
from tkinter import *

def read():
    s1=t1.get()
    s2=t2.get()
    res=s1+s2
    print(res)

win=Tk()
win.geometry("300x300")
l1=Label(win,text="Enter the first string:")
l1.place(x=30,y=40)
t1=Entry(win)
t1.place(x=30,y=60)
l2=Label(win,text="Enter the first string:")
l2.place(x=30,y=100)
t2=Entry(win)
t2.place(x=30,y=120)
b1=Button(win,text="Submit",command=read)
b1.place(x=30,y=150)


win.mainloop()

"""
    
#Qn15a) Write a Python program to draw a hexagon and to fill it with red colour. Explain the turtle methods used in it.
"""
import turtle

tk=turtle.Turtle()
tk.fillcolor("pink")
tk.begin_fill()
for i in range(0,6):
    tk.forward(100)
    tk.right(60)

tk.end_fill()

"""

#Qn15b) Write a python program to convert a colour image to black and white image. Explain the image methods used in it.

"""
from PIL import Image

im=Image.open("Hello.gif")
im=im.convert("RGB")

wi,he = im.size
gr=Image.new("L",im.size)

for h in range(0,he):
    for w in range(0,wi):
        r,g,b=im.getpixel((w,h))
        gray=int(r*0.2989 +g*0.5870 + b*0.1140)
        gr.putpixel((w,h),gray)

gr.save("New.gif")
gr.show()
"""

#Qn16a) Write a GUl-based program that allows the user to convert amount in Indian Rupees to amount in Euro.
#The interface should have labeled entry fields for these two values. These components should be arranged in a grid where the labels occupy the first row and the corresponding fields occupy the second row.
#At start-up, the Rupees field should contain 0.0, and the Euro field should contain 0.0. The third row in the window contains two command buttons, labeled R->E and E->R. 
#When the user presses the first buffon, the program should use the data in the Rupee field to compute the amount in Euro, which should then be output to the Euro field. The second button should perform the inverse function.

"""
from tkinter import *

win=Tk()
win.geometry("450x300")
def re():
    v1=t1.get()
    ans1=int(v1)*0.32
    ans=str(ans1)
    t2.delete(0,'end')
    t2.insert(0,f"{ans}")
    

def er():
    v2=t2.get()
    anss=int(v2)*0.96
    ans=str(anss)
    t1.delete(0,"end")
    t1.insert(0,f"{ans}")

l1=Label(win,text="Enter the value of Euro to convert")
l1.grid(row=0,column=0)
l2=Label(win,text="Enter the value of Rupee to convert")
l2.grid(row=0,column=1)
t1=Entry(win)
t1.grid(row=1,column=0)
t2=Entry(win)
t2.grid(row=1,column=1)
t2.insert(0,"0.0")
t1.insert(0,"0.0")
b1=Button(win,text="R->E",command=re)
b1.grid(row=2,column=0)
b2=Button(win,text="E->R",command=er)
b2.grid(row=2,column=1)

win.mainloop()
"""
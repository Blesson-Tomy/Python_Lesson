"""
import turtle

t=turtle.Turtle()

t.down()

t.hideturtle()
drawing a square
for i in range(0,4):
    t.forward(100)
    t.right(90)


t.up()

#Qn: Drawing a Hexagon
for i in range(0,6):
    t.forward(100)
    t.right(60)

t.up()


#Qn: Add a colour to a shape

t.begin_fill()

for i in range(0,4):
    t.forward(100)
    t.right(90)
t.fillcolor("red")


t.end_fill()



t.begin_fill()
x=30
for i in range(0,2):
    
    t.forward(100)
    t.right(x)
    t.forward(100)
    t.right(150)

t.fillcolor("red")


t.end_fill()




from tkinter import *

# Create the main window
tk = Tk()

# Create a button with the text "Hello"
button1 = Button(tk, text="Hello")

# Create a Text widget with the initial text "Wroki"
text1 = Text(tk, height=5, width=30)  # Set the size of the Text widget
text1.insert(INSERT, "Wroki")  # Insert initial text into the Text widget

# Pack the button and Text widget
button1.pack()
text1.pack()

# Start the Tkinter event loop
tk.mainloop()
"
""
"""



class parent1:

    def meth1(self, Name):
        print("Hello, I am the Parent1: ", Name)

class child1():

    def meth2(self):
        print("Hello, I am the Parent2!")


class child2(child1):

    def eg(self):
        print("Hello, I am trh child")
        super().meth2()
    
    #def meth2(self):
        #print("Method overriding proved")


hild=child2()
#hild.meth1("Blesson")
hild.eg()
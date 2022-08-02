from tkinter import *

root = Tk()

# Creating label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is John.")
# Showing it on the screen
"""
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)
"""

myLabel1.pack()
myLabel2.pack()


# INPUT FIELDS
e = Entry(root, width=50)
e.pack()

# BUTTONS
def myclick():
    print(e.get())
    myLabel = Label(root,text= "I clicked a button!")
    myLabel.pack()
    
myButton = Button(root, text= "Click me!", padx = 50, pady = 5, command=myclick, bg = "#ffffff", fg="blue") # padx and pady are for resizing the button
myButton.pack()


root.mainloop()
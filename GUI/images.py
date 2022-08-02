from tkinter import *
from PIL import ImageTk, Image
from numpy import size

root = Tk()
root.title("Title Root")
# To set the app icon on the top of the screen
# root.iconbitmap('c:/blablabla/bla.ico')

# To exit the program
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

# To show an image
my_img = ImageTk.PhotoImage(Image.open("profile.png").resize((50, 50)))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()

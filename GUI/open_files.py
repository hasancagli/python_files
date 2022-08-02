from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Viewer Example")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select A File", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename).resize((100, 100)))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()

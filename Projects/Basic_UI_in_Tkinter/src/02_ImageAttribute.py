# Tkinter Image Attribute :-

from tkinter import *
root = Tk()
root.geometry("800x600")
img = PhotoImage(file="assets\LoginPagePreview2.png")
label = Label(image=img)
label.pack()
root.mainloop()

#*******************************

# # For jpg images :-
# from PIL import Image, ImageTk 
# root = Tk()
# root.geometry("800x600")

# # TK does not support jpg images hence we have to install the PIL (pillow) library.
# image = Image.open("assets\LoginPagePreview.jpg")
# photo = ImageTk.PhotoImage(image)
# label = Label(image=photo)
# label.pack()
# root.mainloop()
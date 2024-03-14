# Tkinter Frames :-

from tkinter import *

root = Tk()

root.geometry("600x400")
root.title("Frames")

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

label = Label(f1, text="Tkinter Frames side",font=" Helvetica 10 italic")
label.pack()

f2 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

label = Label(f2, text="Tkinter Frames Upper",font=" Helvetica 8 bold")
label.pack()

root.mainloop()
# Tkinter Geometry :

from tkinter import *

root = Tk()

root.geometry("400x400")
root.minsize(300,300)
root.maxsize(800,600)

test = Label(text="hello! Let's start pyton Tkinter")
test.pack()

root.mainloop()

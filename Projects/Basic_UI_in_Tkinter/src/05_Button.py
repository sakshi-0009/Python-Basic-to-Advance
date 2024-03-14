# Tkinter Buttons :-

from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Tkinter Buttons")

def hello():
    print("Hello TK !")

def images():
    print("These are the avilable images.")

def Adaptix():
    print("We are Adiptix")

def contact():
    print("Thank you ! Visit again !!")


f1 = Frame(root, borderwidth=4, bg="grey", relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw",fill="x")

b1 = Button(f1, fg="red", text="Home", command=hello)
b1.pack(side=LEFT, padx=10)

b2 = Button(f1, fg="red", text="Images", command=images)
b2.pack(side=LEFT, padx=10)

b3 = Button(f1, fg="red", text="About us", command=Adaptix)
b3.pack(side=LEFT, padx=10)

b4 = Button(f1, fg="red", text="Contact us", command=contact)
b4.pack(side=LEFT, padx=10)

root.mainloop()
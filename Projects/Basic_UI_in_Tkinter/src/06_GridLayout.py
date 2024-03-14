# Tkinter Grid Layout :-

from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Tkinter Buttons")

def getvals():
    print("Username: ", uservalue.get())
    print("Password: ", passvalue.get())

user = Label(root, text="Username: ")
password = Label(root, text="Password: ")
user.grid()
password.grid(row=1)

# Tkinter Entey Widgets :-
# variable classes in Tkinter:- BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

b1 = Button(text="Submit", command=getvals).grid()

root.mainloop()
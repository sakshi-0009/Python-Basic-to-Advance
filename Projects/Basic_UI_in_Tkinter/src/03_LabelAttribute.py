# Attributes of Label:- Text, Font, Padding, Border, Color

from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Welcome Page")

# ------ Important Label Options :------

# text = add text 
# bd = background
# fg = foreground  
# font = sets the font -> font=("comicsansms", 30, "bold")
# padx = x padding
# pady = y padding
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text="Heyyyyy there!! How are you all ??",bg="pink", fg="Black",padx=80,pady=15,font=("comicsansms 15 italic"),borderwidth=3,relief=SUNKEN)

left = Label(text="Left box", bg="yellow")
# ------Important pack options :-------

# title_label.pack(side=BOTTOM,anchor="sw")
title_label.pack(side=TOP, fill=X)
# title_label.pack(side=LEFT, fill=Y)

left.pack(anchor="nw",)


title_label.pack()
root.mainloop()
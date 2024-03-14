# Tkinter Checkbuttons snd Entry widgets:- simple Hotel form

from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Checkbuttons")

def getvals():
    print("Form Submitted Successfully!")
    
    print(namevalue.get(), phonevalue.get(), gendervalue.get(), paymentvalue.get(), foodservicevalue.get())

    with open("records.txt","a") as f:
        f.write("Name: " + namevalue.get() + ", Phone: " + phonevalue.get() + ", Gender: " + gendervalue.get() + ", Payment mode: " + paymentvalue.get() + ", Food Service: " + str(foodservicevalue.get()) + "\n")


Label(root, text="Welcome to Tkinter Library", font="comicsansms 15 bold",pady=15).grid(row=0, column=3)

name = Label(root, text="Name: ")
phone = Label(root, text="Phone No: ")
gender = Label(root, text="Gender: ")
payment = Label(root, text="Payment mode: ")

#Pack text for our form:-
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
payment.grid(row=4, column=2)

#Tkinter variables for storing entries:-
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

#Entries for our form:-
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
paymententry = Entry(root, textvariable=paymentvalue)

#Packing the entries:-
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
paymententry.grid(row=4, column=3)

#checkbox:-

foodservice = Checkbutton(text="Want to prebook your meal?", variable=foodservicevalue)
foodservice.grid(row=5, column=3)

# button and packing it and assigning it a command:-

Button(text="Submit", command=getvals).grid(row=6, column=3)
root.mainloop()

  
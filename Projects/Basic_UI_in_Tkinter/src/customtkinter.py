import tkinter as tk

class CustomTkinterApp:
    def __init__(self, master):
        self.master = master
        master.geometry("600x400")
        master.title("Checkbuttons")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Welcome to Tkinter Library", font="comicsansms 15 bold", pady=15).grid(row=0, column=3)

        name = tk.Label(self.master, text="Name: ")
        phone = tk.Label(self.master, text="Phone No: ")
        gender = tk.Label(self.master, text="Gender: ")
        payment = tk.Label(self.master, text="Payment mode: ")

        name.grid(row=1, column=2)
        phone.grid(row=2, column=2)
        gender.grid(row=3, column=2)
        payment.grid(row=4, column=2)

        self.namevalue = tk.StringVar()
        self.phonevalue = tk.StringVar()
        self.gendervalue = tk.StringVar()
        self.paymentvalue = tk.StringVar()
        self.foodservicevalue = tk.IntVar()

        nameentry = tk.Entry(self.master, textvariable=self.namevalue)
        phoneentry = tk.Entry(self.master, textvariable=self.phonevalue)
        genderentry = tk.Entry(self.master, textvariable=self.gendervalue)
        paymententry = tk.Entry(self.master, textvariable=self.paymentvalue)

        nameentry.grid(row=1, column=3)
        phoneentry.grid(row=2, column=3)
        genderentry.grid(row=3, column=3)
        paymententry.grid(row=4, column=3)

        foodservice = tk.Checkbutton(self.master, text="Want to prebook your meal?", variable=self.foodservicevalue)
        foodservice.grid(row=5, column=3)

        tk.Button(self.master, text="Submit", command=self.getvals).grid(row=6, column=3)

    def getvals(self):
        print("Form Submitted Successfully!")
        print(self.namevalue.get(), self.phonevalue.get(), self.gendervalue.get(), self.paymentvalue.get(), self.foodservicevalue.get())

        with open("records.txt","a") as f:
            f.write("Name: " + self.namevalue.get() + ", Phone: " + self.phonevalue.get() + ", Gender: " + self.gendervalue.get() + ", Payment mode: " + self.paymentvalue.get() + ", Food Service: " + str(self.foodservicevalue.get()) + "\n")

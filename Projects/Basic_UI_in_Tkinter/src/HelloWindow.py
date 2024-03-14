# TK Installation : Hello TK!

import tkinter as tk

class Welcome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Welcome Page')
        
        self.root.geometry('600x400')
        
        self.label = tk.Label(self.root,text="")
        self.label.pack(pady=50)
        
        self.hello_button = tk.Button(self.root,text='Click me',command=self.display_message)
        self.hello_button.pack(pady=50)
        
    def display_message(self):
        self.label.config(text='Hello TK')
        
    def run(self):
        self.root.mainloop()
        
if __name__ == '__main__':
    app = Welcome()
    app.run()
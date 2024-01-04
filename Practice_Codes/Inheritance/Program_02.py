# Multiple Inheritance : 

class Parent1:
    def __init__(self):
        print("In comstructor parent-1")

    def dispData(self):
        print("In Display data")

class Parent2:
    def __init__(self):
        print("In constructor parent-2")

    def printData(self):
        print("In printData data")

class Child(Parent1,Parent2):
    pass

obj = Child()
obj.dispData()
obj.printData()
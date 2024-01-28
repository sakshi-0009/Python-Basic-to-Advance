# Operator Overloading :-

class Demo:
    x = 10
    def __eq__(self,obj):
        print("I am here")
        return id(self) == id(obj)

class Memo:
    x = 20

obj1 = Demo()
obj2 = Memo()

print(obj1==obj2)

'''  
I this code, the Demo class has a custom __eq__ method that compares object based on their identity using the id function.
When obj1 == obj2 is called, the custom __eq__ method is executed, printong "I am here"
and returning false because obj1 and obj2 re instances of different class.
'''
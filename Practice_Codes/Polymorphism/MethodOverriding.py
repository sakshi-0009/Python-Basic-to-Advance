'''
Method overriding in python is the process by which Subclass provides a specific implementation for a method already definrd in the Superclass.
This enables the subclass to replace or extend the behaviour of the method inherited form the superclass.

To achieve method overriding in python, the overriding method in the subclass must share the same method signature as the one in superclass.
This includes having the same method name, parameters and return type(or a subtype). 

The 'super()' fuunction is often utilized within the overriding method.
This allows the subclass to invoke the overridden method form the superclass.

'''

class Parent:
    def property(self):
        print("Gold,Car,Banglow")

    def career(self):
        print("Engineering")

class Child(Parent):
    def career(self):
        print("Trader")

obj = Child()
obj.property()
obj.career()
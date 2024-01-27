# Attribute Error :-

# eg.1 :-
class Demo:
    def fun(self):
        print("In fun")

obj = Demo()
# obj.gun()       AttributeError: 'Demo' object has no attribute 'gun'
obj.fun()

# eg.1 :-
class Demo:
    def fun(self):
        print("In fun")

    def gun(self):
        print("In gun")

obj = Demo()
obj.fun()
obj = None
# obj.gun()       AttributeError: 'NoneType' object has no attribute 'gun'
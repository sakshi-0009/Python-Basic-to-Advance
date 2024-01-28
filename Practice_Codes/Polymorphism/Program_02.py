class Demo:
    def fun(self):
        print("In Fun : Demo")

class Memo:
    def gun(self):
        print("In Gun : Memo")

def CallFun(obj):
    if hasattr(obj,'fun'):
        obj.fun()
    elif hasattr(obj,'gun'):
        obj.gun()
    else:
        print("Wrong Object Passed")

obj1 = Demo()
obj2 = Memo()

CallFun(obj1)
CallFun(obj2)
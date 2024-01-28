class Demo:
    def fun(self):
        print("In Fun : Demo")

class Memo:
    def gun(self):
        print("In Gun : Memo")

def CallFun(obj):
    if(id(obj) == id(obj1)):
        obj1.fun()

    elif(id(obj) == id(obj2)):
        obj2.gun()

obj1 = Demo()
obj2 = Memo()

CallFun(obj1)
CallFun(obj2)

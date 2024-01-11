#Diamond Problem : 
class GrandP:
    def Fun(self):
        print("Grand-Parents")

class Parent1(GrandP):
    def Fun(self):
        print("Child of Parent 1")

class Parent2(GrandP):
    pass
    # def Fun(self):
    #     print("Child of Parent 2")

class Child(Parent2, Parent1):
    pass

obj = Child()
obj.Fun()
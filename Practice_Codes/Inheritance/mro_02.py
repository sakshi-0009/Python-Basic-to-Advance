#Diamond Problem : 

class GrandP:
    def Fun(self):
        print("Grand Parents")

class Parent1(GrandP):
    def Fun(self):
        print("Child of Parent 1")

class Parent2(GrandP):
    # def Fun(self):
    #     print("Child of Parent 2")
    pass

class Child(Parent2, Parent1):
    pass

obj = Child()
obj.Fun()
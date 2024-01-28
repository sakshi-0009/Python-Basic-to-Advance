''' Abstract Classes:

Abstract classes, incapable of independent instantiation, serve as blueprints.

They may comprise one or more abstract methods, lacking implementation within the abstract class itself.

Reserved for inheritance, abstract classes necessitate implementation of their abstract methods by subclasses.

These classes are crafted using the 'ABC' (Abstract Base Class) module, utilizing the abstractmethod decorator to declare abstract methods.

'''

from abc import *

class Hyundai(ABC):
    def slogan(self):
        print("Slogan")

    @abstractmethod
    def carType(self):
        pass

class Suv(Hyundai):
    def carType(self):
        print("SUV")

class Sedan(Hyundai):
    def carType(self):
        print("Sedan")

print(type(ABC))
obj1 = Suv()
obj1.carType()

obj2 = Sedan()
obj2.carType()

# obj3 = Hyundai()        TypeError: Can't instantiate abstract class Hyundai with abstract methods carType
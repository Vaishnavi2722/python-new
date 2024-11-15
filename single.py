from abc import ABC, abstractmethod
class grand(ABC):
    def func1(self):
        pass

class Parent(grand):
    def func1(self):
        print("parent class")
 
 
class Child(grand):
    def func1(self):
        print("child class")
 
 
object = Child()
obj=Parent()
object.func1()
obj.func1()
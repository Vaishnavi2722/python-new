from abc import ABC, abstractmethod
class car(ABC):
    def mile(self):
        pass

class tesla(car):
    def mile(self):
        print("mileage is 30kmph")

class suzuki(car):
    def mileage(self):
        print("25kmph")

t=tesla()
t.mile()
s=suzuki()
s.mile()
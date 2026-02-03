from abc import ABC, abstractmethod
class Car(ABC):
    #def mileage(self): #empty methods
        pass #no implementation
class Toyota(Car):
    def mileage(self):
        print("mileage is 20")
class Maruti(Car):
    def mileage(self):
        print("mileage is 24")
t=Toyota()
t.mileage()
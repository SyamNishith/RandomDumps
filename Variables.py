class Car:
    wheels=5 #class variable
    def __init__(self,eng,cc):
        self.eng=eng #instance variable
        self.cc=cc #instance variable
    def carConfig(self):
        print("car config is:",self.cc,self.eng,"wheels are",Car.wheels)
c1=Car("pertrol",1800)
c2=Car("diesel",1400)
c1.carConfig()
c2.carConfig()


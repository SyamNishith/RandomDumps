class BMI:
        def __init__(self,height,weight,age):
            print("this is a init method:")
            self.height=height
            self.weight=weight
            self.age=age
        def details(self):
            print(self.height,self.weight,self.age)
s1=BMI(5.5,62,19)
s2=BMI(5.3,52,19)
print(s1.details())
print(s2.details())

    
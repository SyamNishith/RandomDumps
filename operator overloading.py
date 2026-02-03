class Student:
    def __init__(self,phy,che):
        self.phy=phy
        self.che=che
    def __add__(self, other):
        phy=self.phy+other.phy
        che=self.che+other.che
        s3=Student(phy,che)
        return s3

s1=Student(45,54)
s2=Student(56,46)
s3=s1+s2
print(s3.phy)
print(s3.che)
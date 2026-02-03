class Students:
    college="VIIT"
    def __init__(self,m1,edc,bee) :
        self.m1=m1
        self.edc=edc
        self.bee=bee
    @staticmethod
    def info(): #static method
        print("this is a static method:")
    @classmethod
    def cname(cls):#class method
        return cls.college
    def marks(self): #instance method
        return self.m1+self.edc+self.bee
s1=Students(45,40,41)
s2=Students(47,42,41)
print(Students.cname())
print(s1.marks())
print(s2.marks())
print(Students.info())

    
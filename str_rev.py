'''class Mvgr:
    def mechanical(self):
        print("hai from mvgr mechanical")
m1=Mvgr()
m2=Mvgr()
m1.mechanical()
m2.mechanical()'''
'''class hello:
    def __init__(self,color,engine):
        self.color=color
        self.engine=engine
    def car_confiuration(self):
        print("the configuration is:"+self.color,self.engine)
ferrari=hello("red","v8")
audi=hello("black","v4")
ferrari.car_confiuration()
audi.car_confiuration()'''
'''class Car:
    wheels=5
    def __init__(self,color,engine):
        self.color=color
        self.engine=engine
    def car_config(self):
        print(self.color ,self.engine ,Car.wheels,sep="-")
audi=Car("green","v8")
ferrari=Car("red","v12")
audi.car_config()
ferrari.car_config()'''
'''class Student:
    colege="SVEC"
    def __init__(self,python,java):
        self.python=python
        self.java=java
    @staticmethod
    def message():
        print("we are studying in svec college")
    @classmethod
    def college_details(cls):
        return Student.colege
    def student_marks(self):
        return self.python+self.java
ravi=Student(50,48)
hari=Student(48,47)
print(ravi.student_marks())
print(hari.student_marks())
print(Student.college_details())
#Student.message()'''
class Hello:
    def add(self,a=0,b=0,c=0,d=0):
        if a!=0 and b!=0 and c!=0 and d!=0:
            print(a+b+c+d)
        elif a!=0 and b!=0 and c!=0:
            print(a+b+c)
        elif a!=0 and b!=0:
            print(b+c)
        elif a!=0:
            print(a)
h=Hello()
h.add(1,2)
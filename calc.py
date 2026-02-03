
'''class Car:
    wheels=4#static variable
    def __init__(self,model,engine,color):#instance variables
        self.model=model
        self.engine=engine
        self.color=color
    def car_configuration(self):
        print(self.model,self.color,self.engine,Car.wheels)
ferrari=Car("A1","V8","BLACK")#object1
Audi=Car("A5","V6","RED")#object2
Bmw=Car("A3","V12","BLUE")#object3
ferrari.car_configuration()
Audi.car_configuration()
Bmw.car_configuration()
class College:
    clg="MVGR"#STATIC  VARIABLE
    def __init__(self,branch,course):#instance variables
        self.branch=branch
        self.course=course
    @classmethod
    def college_name(cls):
        print(College.clg)
    def course_details(self):
        print(self.branch,self.course)
    @staticmethod
    def career():
        print("Careeeeerrrrrrrrrr")
m=College("MECH","PYTHON")#creationofobject
m.course_details()#instancemethod
College.college_name()#classmethod
College.career()#staticmethod
class Parent:
    def parentsproperty(self):
        print("10 acres of land")
class children(Parent):#single level inheritance
    def childrenproperty(self):
        print("1 acre of land")
c=children()#object creation
c.childrenproperty()
c.parentsproperty()
class Grandparents:
    def granparentsproperty(self):
        print("100 acres of land")
class Parents(Grandparents):
    def parentsproperty(self):
        print("10 acres of land")
class childern(Parents):
    def childrenproperty(self):
        print("1 acre of land")
c=childern()#objectcreation
c.granparentsproperty()
c.parentsproperty()
c.childrenproperty()
class Airtel:
    def airtel_network(self):
        print("this is airtel network")
class Jio:
    def jio_network(self):
        print("this is jio network")
class Iphone(Airtel,Jio):
    def phone(self):
        print("this is a phone")
i=Iphone()#object creation
i.phone()
i.jio_network()
i.airtel_network()
class A:
    def methodA(self):
        print("this is methodA")
class B(A):
    def methodB(self):
        print("this is methodB")
class C(A):
    def methodC(self):
        print("this is methodC")
b=B()
b.methodB()
b.methodA()
class Semester:
    def Examination(self):
        print("failed in semester")
    def Examination(self):
        print("passed in supply")
s=Semester()#object creation
s.Examination()#calling method
class Mvgr:
    @classmethod
    def add(cls,a=0,b=0,c=0,d=0,e=0):
        if a!=0 and b!=0 and c!=0 and d!=0 and e!=0:
            print(a+b+c+d+e)
        elif a!=0 and b!=0 and c!=0 and d!=0:
            print(a+b+c+d)
        elif a!=0 and b!=0 and c!=0:
            print(a+b+c)
        elif a!=0 and b!=0:
            print(a+b)
        elif a!=0:
            print(a)
m=Mvgr()
m.add(1,2,3,4)
class A:
    def __init__(self):
        print("from super class")
class B(A):
    def __init__(self):
        super().__init__()
        print("from sub class")
b=B()#creating object
class A:
    def __init__(self):
        print("from super class A")
class B:
    def __init__(self):
        print("from super class B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("from subclass c")
c=C()
class Hello:
    def __init__(self,_snapid,_instaid):
        self._snapid=_snapid
        self._instaid=_instaid
    def set_instaid(self,value):
        self._instaid=value
    def set_snapid(self,value):
        self._snapid=value
    def get_snapid(self):
        print(self._snapid)
    def get_instaid(self):
        print(self._instaid)
h=Hello("a","b")
h.set_snapid("dad's little princess")
h.set_instaid("mom's little princess")
h.get_instaid()
h.get_snapid()
from abc import *
class Abstractclass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    def not_abstract_method(self):
        print("this is not abstract method")
class concreteclass(Abstractclass):
    def abstract_method(self):
        print("Abstraction concepts")
a=concreteclass()
a.abstract_method()
a=[1,2,3,4,5,6]
key=int(input("enter the key value:"))
for i in a:
    if i==key:
        print(key,"is found at index",a.index(key))
        break
else:
    print("key is not found")
a=[4,6,3,1,2,8,9]
a.sort()
print(a)
key=int(input("enter the key value:"))
low=0
upper=len(a)-1
while low<=upper:
    mid=(low+upper)//2
    if a[mid]==key:
        print(key,"is found at index",a.index(key))
        break
    elif key<a[mid]:
        upper=mid-1
    elif key>a[mid]:
        low=mid+1
else:
    print("key is not found")
class Hello:
    def __init__(self,a):
        self.__a=a
    def talk(self):
        print(self.__a)
h=Hello(10)
h.talk()
print()
class hello:
    def __init__(self,__a):
        self.__a=__a
    def hai(self):
        print(self.__a)
h=hello(5)
print(h._hello__a)#objdot_classname__variable
class hello:
    def __init__(self,__a):#private variable
        self.__a=__a
    def printer(self,__a):
        print("the value of my variable is:",__a)
h=hello(10)#object creation
#print(h._hello__a)
h.printer(10)
def hello():#method definition
    pass #no implementation
hello()
def hai():
    print("good morining")
hai()
from abc import ABC,abstractmethod
class mechanical(ABC):
    @abstractmethod
    def hello(self):#empty method
        pass
    def hai(self):#concrete method
        print("good morning")
class mvgr(mechanical):#inheriting super class
    def hello(self):#providing implementation
        print("good evening")
m=mvgr()#creating object
m.hello()
m.hai()
l=[1,2,3,4,5,6,7,8,9,10]
key=7
for n in l:
    if n==key:
        print(key,"is found at index " ,l.index(n))
        break
else:
    print(key,"is not found")
l=[9,1,3,2,27,11]#unsorted list
key =int(input("enter the key value:"))
l.sort()
print("the sorted list:",l)
low=0
upper=len(l)-1
while low<=upper:
    mid=(low+upper)//2
    if key==l[mid]:
        print("the key is found at index:",l.index(key))
        break
    elif key > l[mid]:
        low=mid+1
    elif key < l[mid]:
        upper=mid-1
else:
    print(key,"is not found")
l=[56,1,7,17,11,24]#unsorted list
two loops
1>> iterations
2>> internal comparissions
for i in range(len(l)-1):#iterations
    for j in range(len(l)-1):#internal comparission
        if l[j] > l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]#swap the values
print("the sorted list is:",l)
l=[56,1,7,17,11,24]
print("the unsorted list is:",l)
for i in range(len(l)-1):
    min_value=min(l[i:])
    min_value_index=l.index(min_value)
    l[min_value_index],l[i]=l[i],l[min_value_index]
print("the sorted list is:",l)'''
'''sal=int(input("enter the salary:"))
da=(sal*40)/100
ha=(sal*20)/100
print(da)
print(ha)
gross_sal=(sal+da+ha)
print(f"{gross_sal:.2f}")'''
'''n=123
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)'''
'''n = str(123)
m = " "
for i in n:
    m = str(i) + m
print(int(m))
print(type(m))'''
'''def reverse(expression):
    reverse=" "
    for ch in expression:
        if ch=="(":
            ch=")"
        elif ch==")":
            ch="("
        reverse=ch+reverse
    return reverse
print(reverse("m*n+(p-q)+r"))'''
def postifx(expression):
    stack=[]
    expression=" "
    operators=set(['+','-','*','/','^','(',')'])
    priority={"+":1,"-":1,"*":2,"/":2,"^":3}
    for ch in expression:
        if ch not in operators:
            expression=expression+ch
        elif ch=="(":
            stack=stack.append(ch)
        elif ch==")":
            while stack and stack[-1]!=")":
                expression =expression+stack.pop()
        else:
            while stack and stack[-1]!="("and priority[ch]<=priority[stack[-1]]:
                expression=expression+stack.pop()
            stack.append(ch)
while stack:
    stack.append(ch):


    if postifx("m*n+(p-)+r"):
        print("hei is in college")
    else:
        print("n lomgeos")










































































































































































































































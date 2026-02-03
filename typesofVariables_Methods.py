'''class Car:
    wheels=143
    def __init__(self,Engine,Type,Mileage):
        self.Engine=Engine
        self.Type=Type
        self.Mileage=Mileage
    def Cardetails(self):
        print(self.Engine,self.Type,self.Mileage,Car.wheels)
Mclaren=Car("3.5l","diesel","5kmpl")
Amg=Car("3l","petrol","8kmpl")
Mclaren.Cardetails()
Amg.Cardetails()'''
'''class wheels:
    def __init__(self):
        print("this is init method of class wheels")
    def hards(self):
        print("slow speed long durable")
    def softs(self):
        print("fast speed less durable")
class phone(wheels):
    def __init__(self):
        super().__init__()
        print("this is init method of class phone")
    def iphone(self):
        print("this is iphone")
    def android(self):
        print("this is android")
p1=phone()
p1.iphone()
p1.android()'''
'''class college:
    collegename="ENGINEERING COLLEGE"
    def __init__(self,branch):
        self.branch=branch
    def instancemethod(self):
        print(self.branch)
    @classmethod
    def displayclgname(cls):
        print(college.collegename)
    @staticmethod
    def statmethod():
        print("this is static method:")
c1=college("AI&DS")
c1.instancemethod()
college.displayclgname()
c1.statmethod()'''
'''class polymorphism:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
p1=polymorphism()
print(p1.add(10))'''
'''from multipledispatch import dispatch
@dispatch(int,int)
def add(a,b):
    return a+b
@dispatch(int,int,int)
def add(a,b,c):
    return a+b+c
@dispatch(float,float,float)
def add(a,b,c):
    return a+b+c
a=add(5,6)
print(a)
a=add(5,6,7)
print(a)
a=add(5.6,7.8,9.8)
print(a)'''
'''class Demo:
    def __init__(self,instaid,snapid):
        self.__instaid=instaid
        self.__snapid=snapid
    def set_instaid(self,value):
        self.__instaid=value
    def set_snapid(self,value):
        self.__snapid=value
    def get_instaid(self):
        return self.__instaid
    def get_snapid(self):
        return self.__snapid
d1=Demo("vgbhfd","bhngtdfd")
d1.set_instaid("bujjii")
d1.set_snapid("snapperrr")
print(d1.get_instaid())
print(d1.get_snapid())'''
'''s="hi guys very good morning i hope ur doing good myself syam im a 2019 engg graduate specialized in information technology"
s1=s.split(" ")
dict={}
for i in s1:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)'''
'''#tup=(1,2,3,3,5)
#for i in range(50):
l1=[(i,i**3) for i in range(11)]
print(l1)'''
'''s="a boy can do everything for girl"
y=s.split(" ")
dict={}
for i in y:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)'''
'''l=[(i,i**2) for i in range(11)]
print(l)'''
#SingleLevelInheritance:
'''class Father:
    def vehicle(self):
        print("my father has splendor plus bike ")
class Son(Father):
    def vehicle(self):
        super().vehicle()
        print('i  have  TVS XL')
f1=Father()
s1=Son()
s1.vehicle()'''
#prime numbers:
'''def isprime(n):
    n=int(input("enter the number:"))
    if n==1:
        return "prime"
    else:
        for i in range(2,n):
            if n%i==0:
                print(n,"is not a prime")
                break
            else:
                print(n,"is a prime")
                break
a=isprime(5)
print(a)'''
#Fibonacci series:
'''def fibonacci(n):
    n=int(input("enter the number you want to find the fibonacci series of:"))
    n1=0
    n2=1
    if n==1:
        return 0
    else:
        print(n1)
        print(n2)
        for i in range(2,n):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3

a=fibonacci(8)
print(a)'''
#Factorial:
'''def factorial(n):
    fact=1
    n=int(input("enter the number you want to find the factorial of:"))
    for i in range(1,n):
        fact=fact*i
    return fact
a=factorial(10)
print(a)'''
'''#palindrome:
def palindrome(s):
    s=input("enter the string:")
    s1=s[::-1]
    if s==s1:
        print(s,"is a palindrome")
    else:
        print(s,"not a palindrome")
palindrome("helloo")'''
#even_numbers:
'''def even(n):
    n=int(input("enter the range of elements:"))
    numbers=[]
    even=[]
    odd=[]
    for i in range(n):
        s=int(input("enter the numbers:"))
        numbers.append(s)
    print(numbers)
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])
    print("even list is:",even)
    print("odd list is:",odd)
even(1)'''




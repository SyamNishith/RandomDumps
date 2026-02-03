'''def hello():
    print("MVGR-COLLEGE")
hello()
hello()
def sum(a,b):
    print(a+b)
sum(5,6)
def multi(a,*b):
    print(a*b[2])
multi(5,7,8,9)
def haha(hello,hai,byee):
    print(hello+hai)
haha(hello="a",hai="b",byee="c")
def add(**a):
    print(a['d']+a['b'])
add(d=5,b=4,c=5)
def add(clg="Mvgr"):
    print("my college name is:"+clg)
add("KLU")
add("GMR")
add()
def python(l):
    for i in  l:
        print("hello "+i)
l=["mech","python","java"]
python(l)
def mvgr(a,b):
    return a+b
print(mvgr(5,6))
def heee(x,/):
    print(x)
heee(7)
def hiii(*,y):
    print(y)
hiii(y=6)
def mixed(a,b,/,*,c,d):
    print(a+b+c+d)
mixed(5,4,6,6)'
def number(n):
    if n==1:
        return n
    else:
        return n*number(n-1)
print(number(6))
from functools import *
x=lambda a,b:a+b
print(x(5,6))
y=lambda a,b,c:a+b+c
print(y(5,6,7))
z=lambda n:n*(n-1)
print(z(5))
n=[1,2,3,4,5,6,7,8,9,10]
print("Input-List:")
print(n)
print("Even List:")
even=list(filter(lambda n:n%2==0,n))
print(even)
print("Double Values:")
double=list(map(lambda n:n**2,even))
print(double)
sum=reduce(lambda a,b:a+b,double)
print(sum)'''
'''try:
    x=5
    print(x)
except:
    print("Andharu mana valleyy brooo")
else:
    print("Manchodivi broo nuvu")
finally:
    print("sardhukooo inkaaa")'''
'''class Chiii(Exception):
    pass
try:
    a,b=map(int,input("enter the values:").split())
    if a<0 or b<0:
        raise Chiii
    else:
        print(a+b)
except Chiii:
    print("chuskuni ivara babuuu")
else:
    print("okk gooodd")
finally:
    print("chaduvukondi firstuuu")
a=int(input("enter a value:"))
print(a)
try:
    l= [1, 2, 3, 4, 5]
    a,b=map(int,input("enter the values:").split())
    c=a/b
    print(c)
    print(l[6])
except ZeroDivisionError:
    print("pass proper inputs")
    b=1
    c=a/b
    print(c)
else:
    print("good gooodd")
finally:
    print("byeeeeee")
a,b=map(int,input("enter the values:").split())
print(a/b)'''
'''x="Love"
def hello():
    print("haiii "+x)
hello()
def hello():
    x="Love"
    print("hai "+x)
hello()
print(x)
var="GlobalVariable"
def hai():
    var="LocalVariable"
    print("This Is: "+var)
hai()
print("This Is: "+var)
def hai():
    global  var
    var="Hello"
    print("this is :"+var)
hai()
print("this is: "+var)'''
x="Python"
def name():
    x="Syamnishith"

    print("Name is:"+x)
name()
print(x)



















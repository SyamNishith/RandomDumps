import math
from functools import *
'''#dictionaries:
s={"name":"syamnishith",
   "age":25,
   "subject":"python"
}
print(s)
print(len(s))
s["subject"]="java"
print(s)
s.update({"subject":"python"})
print(s)
s["clg"]="svcet"
print(s)
s.update({"clg":"svcet"})
print(s)
print(s.keys())
print(s.values())
print(s.items())
q=s.copy()
print(q)
q.pop("clg")
print(q)
q.popitem()
print(q)
del q["age"]
print(q)
q.clear()
print(q)
for i in q.items():
   print(i)
print(q.get("name"))
s={"a":10,"b":20,"c":30}
mult=1
for i in s.values():
   mult=mult*i
print("result is:",mult)
s={"a":10,"b":20,"c":30}
key=input("enter the key tobe removed:")
if key in s:
   s.pop(key)
   print("key is removed")
   print(s)
else:
   print("key is not present")
n=int(input("enter a number:"))
l1=[]
l2=[]
for i in range(1,n+1):
   l1.append(i)
print("numbers:",l1)
for j in range(1,n+1):
   l2.append(j*j)
print("squares:",l2)
print("the dictionary is:",dict(zip(l1,l2)))
word_list=[]
count=[]
n=int(input("enter the size of  word_list:"))
for i in range(n):
   words=input("enter the words:")
   word_list.append(words)
print(word_list)
for j in word_list:
   d=word_list.count(j)
   count.append(d)
print(count)
print(dict(zip(word_list,count)))
s={"name":"syamnishith",
   "age":25,
   "subject":"python"
}
print(s.keys())
print(s.values())
print(s["name"])
print(s.get("name"))
s={"a":10,
   "b":11,
   "c":12
}
mult=1
sum=0
for i in s.values():
    mult=mult*i
    sum=sum+i
print("multiplicaton is :",mult)
print("additiion is :",sum
n=int(input("emter the number:"))
numbers=[]
squares=[]
for i in range(1,n+1):
    numbers.append(i)
for j in range(1,n+1):
    squares.append(j*j)
print(numbers)
print(squares)
a=dict(zip(numbers,squares))
print(type(a))
n=int(input("enter the size of list:"))
list=[]
for i in range(n):
    v=int(input("enter the values of list:"))
    list.append(v)
print(list)
s=set()
unique=[]
for a in list:
    if a not in s:
        unique.append(a)
        s.add(a)
print(unique)
n=int(input("enter the range:"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)
list=["hello","hai","hai","syam","python"]
word_count=[]
for i in list:
    word_count.append(len(i))
print(dict(zip(list,word_count)))
def sq_num(n):
    for i in n:
        print(i,i*i)
list=[1,2,3,4,5,6,7]
sq_num(list)
def hello(n):
    return n*n
print(hello(5))
def hello():
    print("hello")
    hello()
hello()
a=lambda n:n+2
print(a(5))
l=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda n:n%2==0,l))
print(a)
b=list(map(lambda n:n*2,a))
print(b)
c=reduce(lambda a,b:a+b,b)
print(c)
def factorial(n):
    if n==1:
        return 1
    elif n>1:
        return n*factorial(n-1)
print(factorial(5))
a=input("what is your name:\n")
print(a)
b,c,d=input("enter the values:").split(sep="-")
print(b,c,d)
name = "Alice"
age = 25
print(type(age))
print("hi this is {} and im from {}".format("syam","machilipatnam"))#standard format string
print("hi this is {1} and im from {0}".format("syam","machilipatnam"))#positional arguements
print("hi this is {a} and im from {b}".format(a="syam",b="nishith"))#keyword arguements
print("hi this is \"syam\" and im from \"machilipatnam\"")
print("{0:03d} \n {1:5.2f}".format(0,2345.4321))
print("{:07d}".format(453))
a=[1,2,3,5,8]
b=[1,3,8,9]
c=[3,8,10]
d=[]
for i in a:
    if i in b and i in c:
        d.append(i)
print(d)
a=[1,2,3,5,8]
i=0
j=-1
n=int(input("enter the n value:"))
if n<=a[-1]+a[-2]:
    while i<len(a):
            if a[i]+a[j]==n:
                print({a[i],a[j]})
                break
            elif a[i]+a[j]<n:
                i+=1
            else:
                j-=1
else:
    n=int(input("enter the n value:"))
n=int(input("enter the number:"))
reverse=0
while n>0:
    d=n%10
    reverse=reverse*10+d
    n=n//10
print(reverse)
from math import *
n=int(input("enter the number:"))
temp=n
m=0
while n>0:
    d=n%10
    fact=math.factorial(d)
    m=m+fact
    n=n//10
if temp==m:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
n=int(input("enter the first number:"))
m=int(input("enter the second number:"))
if n<m:
    min=n
else:
    min=m
while True:
    if min%n==0 and min%m==0:
        print("lcm of {0} and {1} is {2}".format(n,m,min))
        break
    else:
        min+=1
n=int(input("enter the number:"))
s=" "
while n!=0:
    last=n%10
    s=s+str(last)
    n=n//10
print(int(s))
n=[1,2,0,0,0,3,6]
zeros=[]
non_zeros=[]
for i in n:
    if i==0:
        zeros.append(i)
    if i!=0:
        non_zeros.append(i)
print(non_zeros+zeros)
s=list(input("enter the string:"))
i=0
j=len(s)-1
while i<j:
    if s[i].isalpha() and s[j].isalpha():
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
        i+=1
        j-=1
    elif not(s[i].isalpha()):
        i+=1
    else:
        j-=1
print(" ".join(s))
n=int(input("enter a decimal number:"))
m=bin(n)
m=str(m)
print(m[2:])
s=input("enter the string:")
s1=set(s)
s1=sorted(s1)
for i in s1:
    print(i,s.count(i),end=" ",sep=":")
n=[10,20,30,40,50]
k=int(input("enter the k value:"))
m=n[k+1:]+n[0:k+1]
print(m)
s=input("enter a string:")
s=s.lower()
b=""
for i in s:
    if i in ['a','e','i','o','u']:
        b=b+'0'
    elif b not in ['a','e','i','o','u']:
        b=b+'1'
print(int(b,2))
import keyword
a=keyword.kwlist
n=input("enter your identifier:")
if n in a:
    print(n,"is a keyword which cannot be used as identifier")
else:
    print(n,"is not a keyword which can be used as identifier")
n=input("enter the lower range:")
m=input("enter the upper range:")
q=len(m)
for i in range(int(n),int(m)+1):
    if q==2:
        print("{:02d}".format(i),end=" ")
    elif q==3:
        print("{:03d}".format(i),end=" ")
    elif q==4:
        print("{:04d}".format(i),end=" ")
def pair(l,n):
    l.sort()
    left=0
    right=len(l)-1
    while left<=right:
        if l[left]+l[right]>n:
            right=right-1
        elif l[left]+l[right]<n:
            left=left+1
        elif l[left]+l[right]==n:
            print("pair values are:",l[left],"&",l[right])
            left=left+1
            right=right-1
l=[1,2,3,5,8,9]
n=int(input("enter the n value:"))
pair(l,n)
#AmazingSubstring:
def amazing_substring(str1):
    vowels="aeiouAEIOU"
    count=0
    for i,char in enumerate(str1):
        if char in vowels:
            count+=len(str1)-i
    return count
str1="abrab"
print(amazing_substring(str1))
def triplets(l,n):
    l.sort()
    for i in range(0,n-2):
        j=i+1
        k=n-1
        while j<k:
            if l[i]+l[j]+l[k]==0:
                print(l[i],l[j],l[k])
                j+=1
                k-=1
            elif l[i]+l[j]+l[k]<0:
                j+=1
            else:
                k-=1
l=[0,-1,2,1,-3]
n=len(l)
triplets(l,n)
l=[3,1,5,4,9,7]
l.sort()
print("sorted array is:",l)
n=len(l)
k=int(input("enter the k value:"))
print("{} smallest value is:".format(k),l[k-1])
print("{} largest values is:".format(k),l[n-k])
def closestpair(l,x):
    left=0
    right=0
    i,j,diff=0,len(l)-1,1000000000
    while i<j:
        if abs(l[i]+l[j]-x) < diff:
            left=l[i]
            right=l[j]
            diff=abs(l[i]+l[j]-x)
        if l[i]+l[j] < x:
            i+=1
        else:
            j-=1
    return left,right
l=[10,22,28,29,30,40]
x=54
print(closestpair(l,x))
def toggle(n,k):
    return n ^(1<<k-1)
print(toggle(2,3))
def compare(a,b):
    if a^b:
        print("not same")
    else:
        print("same")
compare(5,15)
def kthbit_set(n,k):
    if n&(1<<(k-1)):
        print("kth bit is set")
    else:
        print("kth bit is clear")
kthbit_set(5,3)
a=57.87
print(f"{a:_>10}:right alignment")
print(f"{a:#<10}:left alignment")
print(f"{a:|^10}:center alignment")
b=1256
print(f"a+b is:{a+b}")
print(f"{a+b = }")
from datetime import datetime
a=datetime.now()
b=datetime.now()
c=datetime.now()
print(f"{b:%c}") #local time
print(f"{a:time->%H:%M:%S date->%d.%m.%y}")
print(f"{c:%I%p}")'''
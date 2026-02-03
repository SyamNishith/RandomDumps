'''n=int(input("enter the range of fibonacci series:"))
a=0
b=1
if n==1:
    print(a)
elif n>1:
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')'''
'''from functools import *
listt=[12,23,43,56,43,76,78,98,17]
print(listt)
even=list(filter(lambda n:n%2==0,listt))
doubless=list(map(lambda n:n*2,even))
half=reduce(lambda a,b:a*b,doubless)
print(even)
print(doubless)
print(half)'''
def hello(n):
        s=[i for i in n if i%2==0 ]
        print(s)
l=[1,2,3,4,5,6,7,8,9,10]
hello(l)
from _functools import *
List=[19,28,37,46,54,63,72,81,90]
print("List:",List)
even=list(filter(lambda n:n%2==0,List))#filter all the even numbers in the list
print("even:",even)
doubles=list(map(lambda n:n*2,even))#double all the even numbers in the even list
print("doubles:",doubles)
reduse= reduce(lambda a,b:a*b,doubles)#to work with reduce function we have to import functools module
print("reduce:",reduse)#multiply all the even numbers in the list

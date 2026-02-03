from array import *
arr=array('i',[])
n=int(input("enter the size of array:"))
for i in range(n):
    x=int(input("enter the array values:"))
    arr.append(x)
print("the array elements are:")
for e in arr:
    print(e)
value=int(input("enter the value u want to search:"))
print(arr.index(value))
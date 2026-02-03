from numpy import *
a=[[10,20,30],[40,50,60]]
print(a)
print(type(a))
#to convert list into array we use asarray() function
newarr=asarray(a,dtype="int",order="F")
print(newarr)
print(type(newarr))
print("DIMENSION:",ndim(newarr))
print("asarray",newarr)
for i in nditer(newarr):
    print(i)
#using frombuffer:
a=b"hello world" #b is a suffix which represents it is stored as byte with ascii values rather than string
newarr2=frombuffer(a,dtype="S1",count=-1,offset=0) #s1>>> represents string datatype
print("frombuffer",newarr2)
##using fromiter:
a=[10,20,30,40,60,50]
newarr3=fromiter(a,dtype="int",count=6)
print("fromiter",newarr3)
#usingarange():
newarr4=arange(start=0,stop=7,dtype="int")
print("arange()",newarr4)
#usinglinespace():
newarr5=linspace(start=0, stop=8, num=9, endpoint=True, retstep=True, dtype=int)
print("linspace",newarr5)
#usinglogspace():
newarr6=logspace(start=0, stop=8, num=9, endpoint=True, base=10.0, dtype=int)
print("logspace",newarr6)
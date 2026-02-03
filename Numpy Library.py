from numpy import *
zd=array(10)
print("from zero dimensional:",zd)
od=array([10,20,30,40,50])#collection of zero dimensions is called one dimension
print("from one dimensional:",od)
print(od[3])#using one subscript so its one dimension
td=array([[10,20,30],[40,50,60]])#collection of single dimensions is called two dimension
print("from two dimensional:",td)
print(td[1][0])#using two subscripts so its two dimension
thd=array([[[10,20,30],[40,50,60]],[[70,80,90],[11,22,33]]])
print(thd)
print(thd[1][1][2])#using three subscripts so its called three dimension array
a=[10,20,30,40,50] #using asarray for onedimensional
b=asarray(a,dtype=int)
print("from asaaray function:",b)
a=[[10,20,30],[40,50,60]] #for row major we use "C" and for column major order we use "F"
b=asarray(a,dtype=int,order="C")
print(b)
for i in nditer(b):
    print(i)
a=b"WELCOME TO NUMPY LIBRARY"
b=frombuffer(a,dtype="S1",count=10,offset=4) #using frombuffer function
print(b)
print(type(b))
a=[10,20,30,40,50] #using fromiter function
b=fromiter(a,dtype=int)
print(b)
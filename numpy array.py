import numpy as np
#creating array using array function:
'''a=np.array([1,2,3,4])#creation of a list into array
print(a)
print(type(a))
a1=np.array([1,2.3,4,4.5,5])#converts a list of diff dtype into floating array
print(a1)
a2=np.array([1,2,3,4],"complex")#converts int array into complex array
print(a2)'''
#creating array using arange function:
'''b=np.arange(1,10,1,dtype="int")
print(b)
b1=np.arange(1,10,2,dtype="float")
print(b1)
b2=np.arange(15,dtype="complex")
print(b2)
b3=np.arange(3.0)#here start and step values are default
print(b3)'''
#creating array using zeros function:
'''c=np.zeros(5)#create a 1-d array of 5 elements with zeros
print(c)
c1=np.zeros((3,4),dtype="int")#3 rows and 4 columns of zeros of int type
print(c1)
c2=np.zeros((3,4))#3 rows and 4 columns of zeros of float type
print(c2)'''
#creating array using ones function:
'''d=np.ones(5)#create an array of 5 elements with value of 1
print(d)
d1=np.ones((3,3),dtype="int")#create an array of 3rows&3col with value of 1 
print(d1)
d2=np.ones([3,3])
print(d2)'''#create an array of 3rows&3col with val of 1 of float dtype
#create an array using empty function:
'''e=np.empty(3)#creates an array of 3 elements without initializing the entries
print(e)
e1=np.empty([3,4],dtype="int")#create an array of 3 rows and 4 col without initializing the entries 
print(e1)
e2=np.empty([3,3])#create an array of 3 rows and 3 col without initializing the entries with int dtype
print(e2)'''
#create an array using (linearspace)Linspace function:
'''f=np.linspace(1,5)#create an array with  50 elements from 1 to 5 including start and stop values
print(f)
f1=np.linspace(1,15,num=4,dtype="int",retstep=True)
print(f1)
f2=np.linspace(1,20,num=5,dtype="int",retstep="True",endpoint=False)
print(f2)'''
#create an array using eye function:
'''g=np.eye(3,k=0,dtype="int")#create an array with 3rows&col with zeros and the diagonal elements with 1
print(g)
g1=np.eye(3,4,k=1,dtype="int")#create an array with 3rows&4col with zeros and the diagonal elements with 1
print(g1)
g2=np.eye(4)#create an array with 4rows&4col with zeros and the diagonal elements with 1 of float dtype
print(g2)'''
#create an array using identity function:
'''h=np.identity(4)# creates an square matrix of 4 rows&col with zeros except main diagonal of float dtype
print(h)
h1=np.identity(3,dtype="int")# creates an square matrix of 3 rows&col with zeros except main diagonal of int dtype
print(h1)'''
#create an array using random function:
i=np.random.rand(4,4)#create an array of 4rows&col with random float values
print(i)
i1=np.random.randn(4)#create an array of 4 elements with random normally distributed values
print(i1)
i2=np.random.randint(1,5,size=(3,3))#create an array of 3 row&col with random val from 1to4 
print(i2)
i3=np.random.randint(1,6,size=6)#create an array of 6 random elements with values from 1to 6
print(i3)
























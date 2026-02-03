#RESHAPE AND RESIZE:
import numpy as np
'''a=np.arange(10)
print(a)
b=np.reshape(a,(5,2),order="F")#reshape only alters the dimensions of array
print(b)
c=np.arange(12)
d=np.resize(c,(5,3))#resize alters the elements of the array
print(d)
#FLATTEN AND RAVEL:
e=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(e)
f=e.flatten()#flatten a 3d array into 1d array:
print("from flatten row order:",f)
f1=e.flatten(order="F")
print("from flatten column order:",f1)
g=np.ravel(e)#flatten a 3d array into 1d array:
print("from ravel row order:",g)
g1=np.ravel(e,order="F")
print("from ravel column order:",g1)
#transpose:rows to columns and columns to rows:
b=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
a=np.array(b)
print(a)
print("before transpose:",a.shape)
c=np.transpose(a)#default axis
print("after transpose:",c.shape)
print(c)
d=np.transpose(a,axes=(0,2,1))#with axes parameter
print("after transpose:",d.shape)
print(d)
a=np.arange(1,25).reshape(2,4,3)
print("before transpose:",a.shape)
print(a)
b=np.transpose(a)#default axes parameter
print("after transpose:",b.shape)
print(b)
c=np.transpose(a,axes=(1,2,0))
print("after transpose:",c.shape)
print(c)
#splitting && joining:
a=np.arange(5)
b=np.arange(6)
c=np.concatenate((a,b))
print(c)
d=np.arange(10).reshape(2,5)
e=np.arange(6).reshape(2,3)
f=np.concatenate((d,e),axis=1)
print(f)
z=np.arange(8)
x=np.split(z,2)
print(x)
#insert and delete:
a=np.arange(6)
b=np.insert(a,2,6)
print(b)
a1=np.insert(a,2,[1,2,3,4,5])
print(a1)
a=np.arange(6).reshape(2,3)
d=np.insert(a,2,[11,12],axis=1)
print(d)
a=np.arange(10)
b=np.append(a,[11,23,45,67])
print(b)
c=np.arange(6).reshape(2,3)
f=np.append(c,[[6,7,8]],axis=0)
print(f)
d=np.append(c,[[6],[7]],axis=1)
print(d)'''
a=np.arange(10)
b=np.delete(a,2)
print(b)
a1=np.arange(10).reshape(2,5)
a2=np.delete(a1,3,axis=1)
print(a2)

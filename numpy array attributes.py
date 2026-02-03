import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)#returns the array
print(a.ndim)#returns the dimension of array
print(a.shape)#returns the no of rows and columns
b=np.array([1,2,3,4,5])
print(b.shape)#returns no of elements if it is 1d array
print(a.size)#returns the product of shape
print(b.size) 
print(a.itemsize)#returns the length of dtype of the item
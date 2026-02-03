import numpy as np
#matrix multiplication:
'''a=np.matrix("1 2 3;4 5 6;7 8 9")#2d matrix can be created using string notation also
print(a)
b=np.arange(9).reshape(3,3)
print(b)
c=a.dot(b)
print("multiplication of 3*3 matrix:")
print(c)
#inverse of a matrix:
a=np.matrix("11 22;33 44")
print(a)
b=np.linalg.inv(a)
print("inverse of a matrix:")
print(b)
#power of a matrix:
a=np.arange(1,5).reshape(2,2)
print(a)
b=np.linalg.matrix_power(a,2)
print(b)
d=np.linalg.matrix_power(a,0)
print(d)
e=np.linalg.matrix_power(a,-2)
print(e)'''
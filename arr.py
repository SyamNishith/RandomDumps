#to work with array we have to import array module#
# array is nothing but collection of similar type of data values#
# we can only work with one dimensional array using array library#
# to work with 2 and 3 dimensional array we have to import numpy module#
# variable name = array("data type",value)
# here variable name = arr
#data type is int so we mentioned "i"
# data type for float is "f".
# we also have some functions in arrays to know the size of array we use buffer.info
# buffer info will print address of array and also size of array.
# to reverse the array we use reverse function
#example:
from array import * # import of array library
arr=array('i',[5,1,2,3]) # declaration of array
print(arr.buffer_info()) # buffer.info function
arr.reverse() # reverse function
print(arr)
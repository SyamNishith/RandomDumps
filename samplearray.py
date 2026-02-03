from array import *
arr=array('i',[1,2,3,4,5])
newArr=array(arr.typecode,(a for a in arr))
for e in newArr:
    print(e)

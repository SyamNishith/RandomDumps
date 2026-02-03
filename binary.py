list = []
pos=-1
s = int(input("enter the size of list:"))
for i in range(s):
    v = int(input("enter the values of list:"))
    list.append(v)
print("LIST:", list)
list.sort()
print("LIST AFTER SORTING:", list)
n = int(input("enter the number you want to search:"))
def binary(list,n):
    lb=0
    ub=len(list)-1
    i=0
    while lb<=ub:
        mid=(lb+ub)//2
        if list[mid] == n:
            globals()['pos']= mid
            return True
        else:
            if list[mid] < n:
                lb = mid+1
            else:
                ub = mid-1
    return False
if binary(list,n):
    print(n,"found at:",pos+1)
else:
    print(n,"not found:")






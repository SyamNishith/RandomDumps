pos = -1
list = []
s = int(input("enter the size of list:"))
for i in range(s):
    v = int(input("enter the values of list:"))
    list.append(v)
print("List:", list)
list.sort()
print("List after sorting:", list)
b = int(input("enter the number you want to search:"))
def binary(list, b):
    lb = 0
    ub = len(list)-1
    while lb <= ub:
        mid = (lb+ub)//2
        if list[mid] == b:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < b:
                lb = mid+1
            else:
                ub = mid-1
    return False
if binary(list, b):
    print(b, "found at:", pos+1)
else:
    print(b, "not found")






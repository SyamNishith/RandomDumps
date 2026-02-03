list = []
pos = -1
s = int(input("enter the size of list:"))
for i in range(s):
    v = int(input("enter the values of list:"))
    list.append(v)
print("LIST:", list)
n=int(input("enter the number you want to search:"))
def linear(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i+=1
    else:
        return False
if linear(list,n):
    print(n,"found at:",pos+1)
else:
    print(n,"not found")



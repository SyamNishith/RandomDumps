list=[]
pos=-1
s=int(input("enter the size of list:"))
for i in range(s):
    v=int(input("enter the list values:"))
    list.append(v)
print("the list values are:",list)
n=int(input("enter the number u want to search:"))
def linear(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False
if linear(list,n):
    print(list,"the element is found at:",pos)
else:
    print(list,"the element is not found")
    
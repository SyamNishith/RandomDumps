list=[]
s=int(input("enter the size of list:"))
for i in  range(s):
    v=int(input("enter the values of list:"))
    list.append(v)
def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd=count(list)
print("even:{},odd:{}".format(even,odd))

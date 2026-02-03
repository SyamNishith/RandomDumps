list=[ ]
s=int(input("enter the size of list:"))
for i in range (s):
    x=int(input("enter the values of list:"))
    list.append(x)
def numbers(list):
    even=0
    odd=0
    for c in list:
        if c%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd=numbers(list)
print("even:{},odd:{}".format(even,odd))




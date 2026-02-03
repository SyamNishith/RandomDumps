list1=[1,2,3,4,5,5]
key=int(input("enter the key element:"))
flag=False
list2=[]
for i in range(len(list1)):
    if key==list1[i]:
        flag=True
        list2.append(i)
if flag==True:
    print("key element is found at index:")
    for i in list2:
        print(i,end=" ")
else:
    print("key element is not found")
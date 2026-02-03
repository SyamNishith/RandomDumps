list=[7,6,5,3,2,1]
list2=[]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list2.append(list[j])
            break
    if i==len(list)-1:
        list2.append(-1)
print(list2)

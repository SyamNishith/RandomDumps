list=[1,2,0,0,0,3,6]
zero_list=[]
nonzero_list=[]
for i in list:
    if i!=0:
        nonzero_list.append(i)
for j in list:
    if j==0:
        zero_list.append(j)
list=nonzero_list+zero_list
print("modified list is:",list)
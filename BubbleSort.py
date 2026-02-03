list=[10,0,23,56,6]
print("unsorted list is:",list)
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i+1]: #ascending order
            list[i],list[i+1]=list[i+1],list[i]
print("sorted list is:",list)


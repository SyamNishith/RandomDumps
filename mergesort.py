list=[]
nums=int(input("enter the size of list:"))
for i in range(nums):
    v=int(input("enter the list values:"))
    list.append(v)
print("user defined list:",list)
def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        leftlist=list[:mid]
        rightlist=list[mid:]
        mergesort(leftlist)
        mergesort(rightlist)
        i=j=k=0
        while len(leftlist)>i and len(rightlist)>j:
            if leftlist[i]<rightlist[j]:
                list[k]=leftlist[i]
                i+=1
                k+=1
            else:
                list[k]=rightlist[j]
                j+=1
                k+=1
        while len(leftlist)>i:
            list[k]=leftlist[i]
            i+=1
            k+=1
        while len(rightlist)>j:
            list[k]=rightlist[j]
            j+=1
            k+=1
mergesort(list)
print("the sorted list is:",list)
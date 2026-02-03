list=[10,20,30,40]
n=len(list)
k=1
list2=list[:n-k:]
list=list[n-k:]
list3=list+list2
print(list3)
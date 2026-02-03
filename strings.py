a="badbc"
s=set(a)#unique values
print(s)
s=sorted(s)
print(s)
for i in s:
    print(i,a.count(i),end=" ")
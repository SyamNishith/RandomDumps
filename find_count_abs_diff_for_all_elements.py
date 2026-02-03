s=[12,3,14,56,77,13]
n=13
count=0
diff=2
for i in s:
    if (abs(i-n)<=diff):
        count+=1
if count==0:
    print(-1)
else:
    print(count)
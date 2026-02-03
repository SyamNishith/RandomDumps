s=[1,0,1]
count=0
for i in range(len(s)):
    if s[i]==1:
        continue
    elif s[i]==0:
        for j in range(i,len(s)):
            s[j]^=1
        count+=1
print(count)





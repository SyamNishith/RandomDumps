s=[-1,0,1,-4,3,6]
s.sort()
count=0
n=6
#0,2,4
#0,1,5
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        for k in range(j+1,len(s)):
            if s[i]+s[j]+s[k]==n:
                count+=1
                print(s[i],s[j],s[k])
if count==0:
    print("no pair found")



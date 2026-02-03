n=int(input("enter the number:"))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+i
if count == n:
    print(n,":perfect number")
else:
    print(n,":not a perfect number")
n=int(input())
while n>9:
    sum=0
    temp=n
    while temp:
        d=temp%10
        sum+=d
        temp//=10
    n=sum
if n==1:
    print("magic")
else:
    print("nm")
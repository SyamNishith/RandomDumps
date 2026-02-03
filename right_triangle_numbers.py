n=int(input("enter the number of rows:"))
for i in range(n):
    value=i+1
    diff=n-1
    for j in range(i+1):
        print(value,end="  ")
        value+=diff
        diff-=1
    print()
n=int(input("enter the number of your choice:"))
for i in range(2,n):
    if n%i==0:
        print(n,"not a prime")
        break
else:
    print(n,"is a prime")

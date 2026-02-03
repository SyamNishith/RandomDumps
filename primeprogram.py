n=int(input("enter the number:"))
if n==1:
    print(n,"is not a  prime")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"not a prime")
            break
    else:
        print(n,"is a prime")
else:
    print(n,"not a prime")
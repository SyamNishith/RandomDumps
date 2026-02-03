#n=int(input("enter the number of your choice:"))
def prime(n):
    if n==1:
        print(n,"is a prime number")
    else:
        for i in range(2,n):
            if n%i==0:
                print(n,"not a prime")
                break
            else:
                print(n,"is a prime")

prime(8)
prime(9)
prime(10)
prime(11)
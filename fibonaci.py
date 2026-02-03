n=int(input("enter the range of fibonacci series:"))
def fibc(n):
    a=0
    b=1
    if n==1:
        print("0")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fibc(n)


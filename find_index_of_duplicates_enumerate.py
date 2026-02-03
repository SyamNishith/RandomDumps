a=[1,1,1,2,3,1,1]
n=int(input("enter the value:"))
for index,values in enumerate(a):
        if values==n:
            print(index,end=" ")
        elif n not in a:
            print(n,"not in list")
            break

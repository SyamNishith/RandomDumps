num=int(input("enter the number of your choice:"))
for i in range(2,num):
    if num%i==0:
        print(num,"not a prime:")
        break
else:
    print(num,"is a prime")




low=int(input("enter low value:"))
up=int(input("enter upper value:"))
for i in range(low,up+1):
    if up<=99:
        print("{:02d}".format(i),end=" ")
    elif up>=100 and up<=999:
        print("{:03d}".format(i),end=" ")

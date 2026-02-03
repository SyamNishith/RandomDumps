for i in range(5):
    for j in range(i+1):
        print("*",end="  ")
    for k in range(4-i):
        print("-",end="  ")
    print()
print("_____________________________")
for i in range(5):
    for j in range(5-i):
        print("*",end="  ")
    for k in range(i):
        print("-",end="  ")
    print()
print("__________________________")
for i in range(1,6):
    for j in range(i):
        print(j+1,end="  ")
    print()
print("__________________________")
for i in range(5):
    for j in range(5-i):
        print(j+1,end="  ")
    print()
print("_______________________________")
string=input("enter the string:")
length=len(string)
for i in range(length):
    for j in range(length-i):
        print(string[j],end=" ")
    print()
print("__________________________________")
string=input("enter the string:")
length=len(string)
for i in range(length):
    for j in range(i+1):
        print(string[j],end=" ")
    print()
print("_____________________________________")
for i in range(6):
    for j in range(7):
        if (i==0 and j%3!=0) or (i==1 and j%3==0 )or (i-j==2) or (i+j==8):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

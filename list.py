string=input("enter the string:")
print("string length:",len(string))
if len(string)//2==0:
    virat,rohit=string[:len(string)//2],string[len(string)//2:]
else:
    rohit,virat=string[:len(string)//2],string[len(string)//2:]
print(virat)
print(rohit)
viratcount=0
rohitcount=0
i=0
for i in range(len(virat)):
    if ((virat[i]=="a")
         or (virat[i]=="e")
         or (virat[i]=="i")
         or (virat[i]=="o")
         or (virat[i]=="u")
    ):
        viratcount+=1
for i in range(len(rohit)):
    if ((rohit[i]=="a")
         or (rohit[i]=="e")
         or (rohit[i]=="i")
         or (rohit[i]=="o")
         or (rohit[i]=="u")
    ):
        rohitcount+=1
if viratcount>rohitcount:
    print("virat is captain:")
elif viratcount<rohitcount:
    print("rohit is captain:")
elif viratcount==rohitcount:
    (print("virat is captain:"))
    



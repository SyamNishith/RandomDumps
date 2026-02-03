s=input("enter the string:")
n=len(s)
h=n//2
if n%2==0:
    virat_half=s[:h]
    rohit_half=s[h:]
else:
    rohit_half=s[:h]
    virat_half=s[h:]
v=0
for i in virat_half:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        v+=1
print(v)
r=0
for i in rohit_half:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        r+=1
print(r)
if v>r or v==r:
    print("virat wins")
if r>v:
    print("rohit wins")
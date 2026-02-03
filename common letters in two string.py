s1=input("enter the first string:")
s2=input("enter the secons string:")
a=list(set(s1) & set(s2))
for i in a:
    print(i)
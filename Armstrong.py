i=int(input("enter a number:"))
result=0
num=i
digit=len(str(i))
while(i!=0):
        r=i%10
        result=result+(r**digit)
        i=i//10
if num == result:
    print(num,"is a armstrong number")
else:
    print(num,"not a armstrong number:")

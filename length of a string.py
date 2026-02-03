s=input("enter the string:")
def length(s):
    count=0
    for i in range(len(s)):
        count+=1
    return count
print(length(s))
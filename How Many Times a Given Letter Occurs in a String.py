s=input("enter a string:")
ch=input("enter the character:")
def occurence(s,ch):
    count=0
    if len(s)==0:
        print("empty string:")
    else:
        for i in range(len(s)):
            if s[i]==ch:
                count+=1
        return count
print(occurence(s,ch))


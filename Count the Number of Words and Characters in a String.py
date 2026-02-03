s=input("enter the string:")
def number(s):
    ch=0
    word=1
    digit=0
    for i in s:
        if (i.isalpha()):
            ch+=1
        elif i==' ':
            word+=1
        elif (i.isdigit()):
            digit+=1
    return ch,word,digit
print(number(s))
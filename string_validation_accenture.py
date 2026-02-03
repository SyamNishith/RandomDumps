#len of list >4:
#not start with digit
#atleast one capital
#atleast one digit
#no space and /
def validation(s):
    if len(s)<4:
        return False
    if s[0].isdigit():
        return False
    capital=0
    digit=0
    for i in range(len(s)):
        if s[i]>="A" and s[i]<="Z":
            capital+=1
        elif s[i].isdigit():
            digit+=1
        elif s[i]==" "or s[i]=="/":
            return False
    if capital>0 and digit>0:
        return True
    return False
s="a987 abC012"
if validation(s):
    print("valid")
else:
    print("not valid")


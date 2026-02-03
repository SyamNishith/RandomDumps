lower=0
upper=0
digits=0
special_char=0
s="Ac_f$@#9"
if len(s)>=8:
    for i in s:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
        if i.isdigit():
            digits+=1
        if i=="@" or i=="#" or i=="$" or i=="_":
            special_char+=1
if upper>=1 and lower>=1 and digits>=1 and special_char >=1 and upper+lower+digits+special_char==len(s):
    print(s,"is a valid string")
else:
    print("not a valid string:")



from string import *
string=input("enter the string:")
c=input("enter the character you want to replace:")
d=input("enter the character you want to replace with:")
def replace(string):
    return string.replace(c,d)
print(replace(string))

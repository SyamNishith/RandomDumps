from string import ascii_lowercase as asclw
s=input("enter the string:")
def pangram(s):
    return set(asclw) - set(s.lower()) == set([])
if (pangram(s) == True):
    print(s,"is a pangram")
else:
    print("not a pangram")



s=input("enter the string:")
def check(s):
    final = ""
    for i in range(len(s)):
        if i%2 ==0:
            final= final+s[i]
    return final
print("modified string is:",check(s))
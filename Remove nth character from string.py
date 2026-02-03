s=input("enter the string:")
n=int(input("enter the index of character you want to remove:"))
def remove(s,n):
    first = s[:n]
    second = s[n+1:]
    return first + second
print(remove(s,n))

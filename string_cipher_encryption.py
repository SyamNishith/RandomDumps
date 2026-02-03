s="middle-Outz"
print(ord(""))
n=2
new_Str=" "
for i in range(len(s)):
    if s[i].isalpha():
        change=ord(s[i])
        if change>=65 or change<=88:
            new_Str+=chr(change+n)
        elif change>=89:
            new_Str+=chr(change+65)
    else:
        new_Str+=s[i]
print(new_Str)



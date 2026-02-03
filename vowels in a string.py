s=input("enter the string:")
def count(s):
    vowels=0
    nonvowels=0
    for i in s:
        if (i=='a'or i =='e'or i =='i' or i =='o'or i =='u'):
            vowels+=1
        else:
            nonvowels+=1
    return vowels,nonvowels
print(count(s))
    
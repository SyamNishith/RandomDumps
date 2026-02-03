def automorphic(number):
    square=number*number
    print(square)
    while number:
        if number%10!=square%10:
            return False
        else:
            number//=10
            square//=10
    return True
n=int(input("enter a number:"))
if automorphic(n):
    print(n,"is automorphic")
else:
    print(n,"is not automorphice")
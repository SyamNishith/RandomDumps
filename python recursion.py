def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
n=6
print("factorial of the number is",n,"is",factorial(n))

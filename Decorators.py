def sub(a,b):
    print(a-b)
def decorator(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
sub=decorator(sub)
sub(8,10)
print(sub)
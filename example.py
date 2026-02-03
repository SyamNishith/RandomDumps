a=56#global variable
def hello():
    globals()['a']=1256#to access gvariable we use globals()method
    a=25#local variable
    print(a)
hello()
print(a)#we can access global variable anywhere
#print(a)#we cannot access local variable outside function
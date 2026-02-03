a=19
def variable():
    a=21
    x=globals()['a']
    globals()['a']=20
    print("local variable:",a)
variable()
print("global variable:",a)



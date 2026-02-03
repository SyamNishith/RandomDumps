#python does not support method overloading
#directly so we will use default arguments.
class calc:
    def add(self,x=0,y=0,z=0):
        if x!=0 and y!=0 and z!=0: #default arguments
            res=x+y+z
        elif x!=0 and y!=0:
            res=x+y
        else:
            res=x
        return res
c=calc()
res=c.add(10)
print(res)

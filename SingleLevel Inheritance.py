class A:
    @staticmethod
    def a1():
        print("hello from a1 method of class A")
class B(A):
    pass
    #def a2():
        #print("hello from a2 method of class B")
a=B()
a.a1()
#a.a2()
class A:
    @staticmethod
    def a1():
        print("hello from a1 method of class A")       
class B(A):
    @staticmethod
    def a2():
        print("hello from a2 method of class B")
class C(B):
    @staticmethod
    def a3():
        print("hello from a3 method of class c")
a=C()
a.a1()
a.a2()
a.a3()
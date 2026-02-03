class A:
    def first(self):
        print("this is first method of class A:")
    def second(self):
        print("this is second method of class A:")
class B():
        def third(self):
            print("this is third method of class B:")
        def fourth(self):
            print("this is fourth method of class B:")

class C(A,B):
    def fifth(self):
        print("this is fifth method of class C:")

c=C()
c.first()
b=B()
b.third()
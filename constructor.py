class A:
    def __init__(self):
        print("from class A init:")
    def one(self):
        print("one:")
    def two(self):
        print("two:")
class B():
    def __init__(self):
        print("from class B init:")
    def three(self):
        print("three:")
    def four(self):
        print("four:")
class C(A,B):
    def __init__(self):
        super().
        print("from class c init:")
    def five(self):
        print("five:")
a=C()




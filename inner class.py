class one:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.e2=self.two(35,8)
    def show(self):
        print("name:",self.name,"id:",self.id)
        self.e2.prof()
    class two:
        def __init__(self,age,exp):
            self.age=age
            self.exp=exp
        def prof(self):
            print("age:",self.age,"exp:",self.exp)
e1=one('leo',56)
print(e1.id)
print(e1.show())
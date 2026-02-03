class Employee():
    def __init__(self,first,last,id,pay):
        self.first=first
        self.last=last
        self.id=id
        self.pay=pay
        self.mail=first+last+'@gmail.com'
    def fullname(self):
        return(("fullname:{}{}".format(self.first,self.last)))
emp1=Employee("syam","nishith",121,123)
emp2=Employee("nishith","syam",142,654)
print("Id:",emp1.id)
print("Pay:",emp1.pay)
print("first:",emp1.first)
print("last:",emp1.last)
print(emp1.fullname())
print("mail id:",emp1.mail)



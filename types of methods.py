class employee:
    office="IBM"
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def Edetails(self): #instance method
        return ("{} {}".format(self.name,self.id))
    def getname(self): #Accessors or Access methods
        return self.name
    def getid(self): ##Accessors or Access methods
        return self.id
    def setname(self,value): #Setter Method
         self.name=value
    @classmethod
    def info(cls):
         return cls.office
    @staticmethod
    def new():
        print("this is a static method of employee class:")
emp1=employee("leo",1203)
emp2=employee("car",1205)
print(emp1.getname())
print(emp1.getid())
emp1.setname('aiden')
print(emp1.getname())
print(employee.info())
print(emp1.new())
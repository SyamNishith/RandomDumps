class Class:
    school="chaitanya" #static variable or class variable
    def __init__(self,marks,attendance,):
        self.marks=marks # instance variable
        self.attendance=attendance # instance variable

s1=Class(75,85)
s2=Class(80,90)
s3=Class(90,95)
print(s1.marks)
print(Class.school)


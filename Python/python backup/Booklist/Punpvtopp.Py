class student:
    No_Of_Stu=5
    _protect=10
    __private=20
    def __init__(self,aname,aprofession,asalary):
        self.name=aname
        self.profession=aprofession
        self.salary=asalary
    def student2(self):
        return f"My name is {self.name}"

    @classmethod
    def change_no_of_student2(cls,number):
        cls.No_Of_Stu=number
        return number
    @staticmethod
    def statcheck():
        print("My Name is afridi")
class student2(student):
    def __init__(self,aname,aproff,asal):
        self.name=aname
        self.profession=aproff
        self.salary=asal
Afridi=student("SK MD AFRIDI","Python Developer",50000)
Ronit=student2("Ronit Bask","Python Developer",50000)
print(Afridi._protect)
print(Ronit._protect)
print(Ronit._student__private)
print(Ronit.No_Of_Stu)